# This file contains the functions for the different pieces, returning avaliable squares for a board size M x N.
"""
Returns list of tuples with available squares for a given position
    M is number of rows, N is number of columns, board is list
"""

import math
from create_board import create_initial_positions
from edge_checker import column
from squares import *
from piece_threats import *

## TODO use squares_avaliable in squares and delete this file.
# King, Queen, , Rook, Bishop, Knight get a function to define what pieces they threaten on M x N board
# Function takes M,N, List of Array of available squares and outputs list of arrays updated available squares for each position on avaliable squares.
# Basic function structure repeated for each piece type

def king_position_avaliable( M,N, board ):
    """ M is number of rows, N is number of columns, board is list
        Calculate avaliable positions at each king position by removing unavailable squares.
    """
    king_values_list=[]
    i=1
    for i in board:
        avaliable_squares = create_set(board)
        threatened=create_threatened(i)
        current_column = column(i,N)

        # This is the only line that changes, so instead single function for all pieces and then this line can be switch.
        threatened=king_threats(N,i,current_column,threatened)

        # Remove squares above or below the board
        threatened=trim_threatened(threatened,M*N)
        
        # remove threatehented squares
        avaliable_squares = update_avaliable_squares(threatened, avaliable_squares)

        # key is a list of squares with pieces in it
        king_values_list.append((frozenset({i}),frozenset(avaliable_squares)))
    
    return (king_values_list)

def knight_position_avaliable( M,N, board ):

    i=0
    knight_values_list = []
    for i in board:
        # calculate avaliable positions at each knight position by removing unavailable squares.
        avaliable_squares = set(board)

        threatened = set()
        # Not threatened but must also be removed from threatened squares
        threatened.add(i)
        
        #Only this part changes for each piece so maybe new function with only this.

        current_column = column(i,N)
        current_row = math.ceil(i/N)

        if column(i+2*N+1,N) == current_column+1:
            threatened.add(i+2*N+1)
            threatened.add(i-2*N+1)

        
        if column(i+2*N-1,N) == current_column-1:
            threatened.add(i+2*N-1)
            threatened.add(i-2*N-1)
        
        if column(i+N-2,N) == current_column-2:
            threatened.add(i+N-2)
            threatened.add(i-N-2)

        if column(i+N+2,N) == current_column+2:
            threatened.add(i+N+2)
            threatened.add(i-N+2)

        # Remove squares above or below the board
        for elem in list(threatened):
            if elem <= 0:
                threatened.discard(elem)
        for elem in list(threatened):
            if elem > M*N:
                threatened.discard(elem)

        avaliable_squares.difference_update(threatened)
        knight_values_list.append((frozenset({i}),frozenset(avaliable_squares)))

    
    return (knight_values_list)

def rook_position_avaliable( M,N, board ):
    """ M is number of rows, N is number of columns, board is list, dict? with avaliable board positions
    """
    i=0
    rook_values_list = []
    
    for i in board:
        # calculate avaliable positions at each rook position by removing unavailable squares.
        avaliable_squares = set(board)
        threatened = set()
        # Not threatened but must also be removed from threatened squares
        threatened.add(i)
        
        current_column = (i%N)
        current_row = math.ceil(i/N)

        # Horizontal
        for t in range (1,N):
            if math.ceil((i+t)/N) == current_row:
                threatened.add(i+t)
            if math.ceil((i-t)/N) == current_row:
                threatened.add(i-t)
        
        # Vertical
        for t in range (1,M):
            # Need 0 because last column has no remainder
            if math.ceil((i+(t*N))%N) == current_column|0:
                threatened.add(i+(t*N))
                #print(f'Added: {i+(t*N)}')
            if math.ceil((i-(t*N))%N) == current_column|0:
                threatened.add(i-(t*N))
             
        # Remove squares above or below the board
        for elem in list(threatened):
            if elem <= 0:
                threatened.discard(elem)
        for elem in list(threatened):
            if elem > M*N:
                threatened.discard(elem)


        avaliable_squares.difference_update(threatened)
        rook_values_list.append((frozenset({i}),frozenset(avaliable_squares)))
    
    return (rook_values_list)

def bishop_position_avaliable( M,N, board ):
    """ 
    Returns set of tuples with available squares for a given position
    M is number of rows, N is number of columns, board is list of values on board
    """
    i=0
    bishop_values_list=[]
    
    for i in board:
        avaliable_squares = set(board)
        # calculate avaliable positions at each bishop position by removing unavailable squares.
        threatened = set()
        # Not threatened but must also be removed from threatened squares
        threatened.add(i)
        
        current_column = column(i,N)
        current_row = math.ceil(i/N)

        # Diagonal is limted by shortest side
        shortest_side = min(M,N)
        for t in range (1,shortest_side):
            #print(f'i: {i}, current_column: {current_column}, current_row: {current_row}')
            # column must be greater than i column
            if column(i+N*t+t,N) > current_column:
                threatened.add(i+N*t+t)
            if column(i-N*t+t,N) > current_column:
                threatened.add(i-N*t+t)

            # column must be less than i column
            if column(i+N*t-t,N) < current_column:
                threatened.add(i+N*t-t)
            if column(i-N*t-t,N) < current_column:
                threatened.add(i-N*t-t)
        
        # Remove squares above or below the board
        for elem in list(threatened):
            if elem <= 0:
                threatened.discard(elem)
        for elem in list(threatened):
            if elem > M*N:
                threatened.discard(elem)

        avaliable_squares.difference_update(threatened)
        bishop_values_list.append((frozenset({i}),frozenset(avaliable_squares)))
    return (bishop_values_list)

def queen_position_avaliable( M,N, board ):
    """ Combine bishop with rook
    """
    i=0
    queen_values_list = []

    for i in board:
 # calculate avaliable positions at each bishop position by removing unavailable squares.
        avaliable_squares = set(board)
        threatened = set()
        # Not threatened but must also be removed from threatened squares
        threatened.add(i)
        
        # Rook squares 
        # TODO refactor to use threats calcs as own functions
        current_column = (i%N)
        current_row = math.ceil(i/N)

        # Horizontal
        for t in range (1,N):
            if math.ceil((i+t)/N) == current_row:
                threatened.add(i+t)
            if math.ceil((i-t)/N) == current_row:
                threatened.add(i-t)
        
        # Vertical
        for t in range (1,M):
            # Need 0 because last column has no remainder
            if math.ceil((i+(t*N))%N) == current_column|0:
                threatened.add(i+(t*N))
                #print(f'Added: {i+(t*N)}')
            if math.ceil((i-(t*N))%N) == current_column|0:
                threatened.add(i-(t*N))
       
        current_column = column(i,N)
        current_row = math.ceil(i/N)

        # Bishop squares
        # Diagonal is limted by shortest side
        shortest_side = min(M,N)
        for t in range (1,shortest_side):
            #print(f'i: {i}, current_column: {current_column}, current_row: {current_row}')
            # column must be greater than i column
            if column(i+N*t+t,N) > current_column:
                threatened.add(i+N*t+t)
            if column(i-N*t+t,N) > current_column:
                threatened.add(i-N*t+t)

            # column must be less than i column
            if column(i+N*t-t,N) < current_column:
                threatened.add(i+N*t-t)
            if column(i-N*t-t,N) < current_column:
                threatened.add(i-N*t-t)
       
        # Remove squares above or below the board
        for elem in list(threatened):
            if elem <= 0:
                threatened.discard(elem)
        for elem in list(threatened):
            if elem > M*N:
                threatened.discard(elem)

        avaliable_squares.difference_update(threatened)
        queen_values_list.append((frozenset({i}),frozenset(avaliable_squares)))
    
    return (queen_values_list)
