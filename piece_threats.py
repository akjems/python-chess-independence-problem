from board import column

import math

def create_threatened(i):
    threatened = set()
    threatened.add(i)
    return (threatened)

def trim_threatened(threatened,board_size):
    """ Remove squares over or below the board"""
    for elem in list(threatened):
        if elem <= 0:
            threatened.discard(elem)
    for elem in list(threatened):
        if elem > board_size:
            threatened.discard(elem)
    return(threatened)

def king_threats (M,N,i, current_column, threatened):

    if column(i+1,N) > current_column:
        threatened.add(i+1)
        threatened.add(i+N+1)
        threatened.add(i-N+1)
    if column(i-1,N) < current_column:     
        threatened.add(i-1)
        threatened.add(i+N-1)
        threatened.add(i-N-1)
    if column(i+N,N) == current_column:
        threatened.add(i+N)
    if column(i-N,N) == current_column:
        threatened.add(i-N)
    return (threatened)

def bishop_threats (M,N,i, current_column, threatened):
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
    
    return (threatened)

def rook_threats (M,N,i,current_column, threatened):
    # Horizontal threats
    current_row = math.ceil(i/N)
    for t in range (1,N):
        if math.ceil((i+t)/N) == current_row:
            threatened.add(i+t)
        if math.ceil((i-t)/N) == current_row:
            threatened.add(i-t)    
    # Vertical threats
    for t in range (1,M):
        # Need 0 because last column has no remainder
        if math.ceil((i+(t*N))%N) == current_column or math.ceil((i+(t*N))%N) ==  0:
            threatened.add(i+(t*N))
        if math.ceil((i-(t*N))%N) == current_column or math.ceil((i-(t*N))%N) ==  0:
            threatened.add(i-(t*N))
    return (threatened)

def knight_threats (M,N,i,current_column, threatened):
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
    return (threatened)


def queen_threats(M, N,i, current_column, threatened):
    threatened=bishop_threats(M,N,i,current_column,threatened)
    threatened=rook_threats(M,N,i,current_column,threatened)
    return(threatened)