# This file contains the functions for the different pieces, returning avaliable squares for a board size M x N.
"""
Returns list of tuples with available squares for a given position
    M is number of rows, N is number of columns, board is list
"""
#TODO Have king, queen, rook return list instead of dictionary

import math
from create_board import create_initial_positions
from edge_checker import column

## TODO i should always start at 1
# King, Queen, , Rook, Bishop, Knight get a function to define what pieces they threaten on M x N board
# Function takes M,N, List of Array of available squares and outputs list of arrays updated available squares for each position on avaliable squares.
# Basic function structure repeated for each piece type

def king_position_avaliable( M,N, board ):
    """ M is number of rows, N is number of columns, board is list, dict? with avaliable board positions
    """
    
    king_values_dict = {}
    i=1
    for i in board:
        # calculate avaliable positions at each king position by removing unavaiable squares.
        avaliable_squares = []
        threatened = []
        # Not threatened but must also be removed from threatened squares
        threatened.append(i)
        
        current_column = column(i,N)
        current_row = math.ceil(i/N)

        #Only this part changes for each piece so maybe new function with only this.
        if column(i+1,N) > current_column:
            threatened.append(i+1)
            threatened.append(i+N+1)
            threatened.append(i-N+1)
        if column(i-1,N) < current_column:     
            threatened.append(i-1)
            threatened.append(i+N-1)
            threatened.append(i-N-1)
        
        if column(i+N,N) == current_column:
            threatened.append(i+N)
        if column(i-N,N) == current_column:
            threatened.append(i-N)

        # Remove squares above or below the board
        threatened = [item for item in threatened if item > 0]
        threatened = [item for item in threatened if item <= M*N]

        avaliable_squares = [x for x in board if x not in threatened]
 
        # key is a list of squares with pieces in it
        king_values_dict[i]=avaliable_squares
    
    return (king_values_dict)

def knight_position_avaliable( M,N, board ):
    """ M is number of rows, N is number of columns, board is list, dict? with avaliable board positions
    """
    i=0
    knight_values_dict = {}
    knight_values_list = []
    for i in board:
        # calculate avaliable positions at each knight position by removing unavailable squares.
        avaliable_squares = []
        threatened = []
        # Not threatened but must also be removed from threatened squares
        threatened.append(i)
        
        #Only this part changes for each piece so maybe new function with only this.

        current_column = column(i,N)
        current_row = math.ceil(i/N)

        if column(i+2*N+1,N) == current_column+1:
            threatened.append(i+2*N+1)
            threatened.append(i-2*N+1)

        
        if column(i+2*N-1,N) == current_column-1:
            threatened.append(i+2*N-1)
            threatened.append(i-2*N-1)
        
        if column(i+N-2,N) == current_column-2:
            threatened.append(i+N-2)
            threatened.append(i-N-2)

        if column(i+N+2,N) == current_column+2:
            threatened.append(i+N+2)
            threatened.append(i-N+2)

        # Remove squares above or below the board
        threatened = [item for item in threatened if item > 0]
        threatened = [item for item in threatened if item <= M*N]

        avaliable_squares = [x for x in board if x not in threatened]
 
        knight_values_dict[i]=avaliable_squares
        knight_values_list.append(([i],avaliable_squares))

    
    return (knight_values_list)

def rook_position_avaliable( M,N, board ):
    """ M is number of rows, N is number of columns, board is list, dict? with avaliable board positions
    """
    i=0
    rook_values_dict = {}
    for i in board:
        # calculate avaliable positions at each rook position by removing unavailable squares.
        avaliable_squares = []
        threatened = []
        # Not threatened but must also be removed from threatened squares
        threatened.append(i)
        
        current_column = (i%N)
        current_row = math.ceil(i/N)

        # Horizontal
        for t in range (1,N):
            if math.ceil((i+t)/N) == current_row:
                threatened.append(i+t)
            if math.ceil((i-t)/N) == current_row:
                threatened.append(i-t)
        
        # Vertical
        for t in range (1,M):
            # Need 0 because last column has no remainder
            if math.ceil((i+(t*N))%N) == current_column|0:
                threatened.append(i+(t*N))
                #print(f'Added: {i+(t*N)}')
            if math.ceil((i-(t*N))%N) == current_column|0:
                threatened.append(i-(t*N))
      
        # Remove squares above or below the board
        threatened = [item for item in threatened if item > 0]
        threatened = [item for item in threatened if item <= M*N]


        avaliable_squares = [x for x in board if x not in threatened]
 
        rook_values_dict[i]=avaliable_squares
    
    return (rook_values_dict)

def bishop_position_avaliable( M,N, board ):
    """ 
    Returns list of tuples with available squares for a given position
    M is number of rows, N is number of columns, board is list
    """
    i=0
    bishop_values_dict = {}
    bishop_values_list=[]
    for i in board:
        # calculate avaliable positions at each bishop position by removing unavailable squares.
        avaliable_squares = []
        threatened = []
        # Not threatened but must also be removed from threatened squares
        threatened.append(i)
        
        current_column = column(i,N)
        
        current_row = math.ceil(i/N)

        # Diagonal is limted by shortest side
        shortest_side = min(M,N)
        for t in range (1,shortest_side):
            #print(f'i: {i}, current_column: {current_column}, current_row: {current_row}')
            # column must be greater than i column
            if column(i+N*t+t,N) > current_column:
                threatened.append(i+N*t+t)
            if column(i-N*t+t,N) > current_column:
                threatened.append(i-N*t+t)

            # column must be less than i column
            if column(i+N*t-t,N) < current_column:
                threatened.append(i+N*t-t)
            if column(i-N*t-t,N) < current_column:
                threatened.append(i-N*t-t)
       
        # Remove squares above or below the board
        threatened = [item for item in threatened if item > 0]
        threatened = [item for item in threatened if item <= M*N]

        #print(f'{i} : {threatened}')
        avaliable_squares = [x for x in board if x not in threatened]
 
        #bishop_values_dict[i]=avaliable_squares
        bishop_values_list.append(([i],avaliable_squares))
    
    return (bishop_values_list)

def queen_position_avaliable( M,N, board ):
    """ Combin bishop with rook
    """
    i=0
    queen_values_dict = {}

    for i in board:
 # calculate avaliable positions at each bishop position by removing unavailable squares.
        avaliable_squares = []
        threatened = []
        # Not threatened but must also be removed from threatened squares
        threatened.append(i)
        
        # Rook squares 
        # TODO refactor to use threats calcs as own functions
        current_column = (i%N)
        current_row = math.ceil(i/N)

        # Horizontal
        for t in range (1,N):
            if math.ceil((i+t)/N) == current_row:
                threatened.append(i+t)
            if math.ceil((i-t)/N) == current_row:
                threatened.append(i-t)
        
        # Vertical
        for t in range (1,M):
            # Need 0 because last column has no remainder
            if math.ceil((i+(t*N))%N) == current_column|0:
                threatened.append(i+(t*N))
                #print(f'Added: {i+(t*N)}')
            if math.ceil((i-(t*N))%N) == current_column|0:
                threatened.append(i-(t*N))
       
        current_column = column(i,N)
        current_row = math.ceil(i/N)

        # Bishop squares
        # Diagonal is limted by shortest side
        shortest_side = min(M,N)
        for t in range (1,shortest_side):
            #print(f'i: {i}, current_column: {current_column}, current_row: {current_row}')
            # column must be greater than i column
            if column(i+N*t+t,N) > current_column:
                threatened.append(i+N*t+t)
            if column(i-N*t+t,N) > current_column:
                threatened.append(i-N*t+t)

            # column must be less than i column
            if column(i+N*t-t,N) < current_column:
                threatened.append(i+N*t-t)
            if column(i-N*t-t,N) < current_column:
                threatened.append(i-N*t-t)
       
        # Remove squares above or below the board
        threatened = [item for item in threatened if item > 0]
        threatened = [item for item in threatened if item <= M*N]

        #print(f'{i} : {threatened}')
        avaliable_squares = [x for x in board if x not in threatened]
 
        queen_values_dict[i]=avaliable_squares
   
 
    
    return (queen_values_dict)
