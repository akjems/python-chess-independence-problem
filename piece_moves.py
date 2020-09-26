
import math
from create_board import create_initial_positions

# King, Queen, , Rook, Bishop, Knight get a function to define what pieces they threaten on M x N board

# Function takes M,N, List of Array of available squares and outputs list of arrays updated available squares for each position on avaliable squares.


# Basic function structure repeated for each piece type



def king_position_avaliable( M,N, board ):
    """ M is number of rows, N is number of columns, board is list, dict? with avaliable board positions

    TODO remove position if king on left right edges of board, use N values.
    """
    
    king_values_dict = {}
    i=0
    for i in board:
        # calculate avaliable positions at each king position by removing unavaiable squares.
        avaliable_squares = []
        threatened = []
        # Not threatened but must also be removed from threatened squares
        threatened.append(i)
        
        #Only this part changes for each piece so maybe new function with only this.
        threatened.append(i+N)
        threatened.append(i-N)
        threatened.append(i+1)
        threatened.append(i-1)
        threatened.append(i+N+1)
        threatened.append(i+N-1)
        threatened.append(i-N+1)
        threatened.append(i-N-1)

        # Remove squares above or below the board
        threatened = [item for item in threatened if item > 0]
        threatened = [item for item in threatened if item <= M*N]

        #print(f'{i} : {threatened}')
        avaliable_squares = [x for x in board if x not in threatened]
 
        # key is a list of squares with pieces in it
        king_values_dict[i]=avaliable_squares
    
    return (king_values_dict)

def knight_position_avaliable( M,N, board ):
    """ M is number of rows, N is number of columns, board is list, dict? with avaliable board positions

    TODO remove position if king on edge of board, use M & N values
    """
    i=0
    knight_values_dict = {}
    for i in board:
        # calculate avaliable positions at each knight position by removing unavailable squares.
        avaliable_squares = []
        threatened = []
        # Not threatened but must also be removed from threatened squares
        threatened.append(i)
        
        #Only this part changes for each piece so maybe new function with only this.
        threatened.append(i+2*N+1)
        threatened.append(i+2*N-1)
        threatened.append(i+N-2)
        threatened.append(i-N-2)
        threatened.append(i-2*N-1)
        threatened.append(i-2*N+1)
        threatened.append(i-N+2)
        threatened.append(i-N-2)

        # Remove squares above or below the board
        threatened = [item for item in threatened if item > 0]
        threatened = [item for item in threatened if item <= M*N]

        print(f'{i} : {threatened}')
        avaliable_squares = [x for x in board if x not in threatened]
 
        knight_values_dict[i]=avaliable_squares
    
    return (knight_values_dict)

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
            # Need to check I am in the same row as i,
            #print(f'')
            #print(f'current_row: {current_row}: i = {i}: t = {t}: math.ceil((i+t)/N)={math.ceil((i+t)/N)}')
            #print(f'i+t: {i+t}')
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

        print(f'{i} : {threatened}')
        avaliable_squares = [x for x in board if x not in threatened]
 
        rook_values_dict[i]=avaliable_squares
    
    return (rook_values_dict)

def bishop_position_avaliable( M,N, board ):
    """ M is number of rows, N is number of columns, board is list, dict? with avaliable board positions
    """
    i=0
    bishop_values_dict = {}
    for i in board:
        # calculate avaliable positions at each bishop position by removing unavailable squares.
        avaliable_squares = []
        threatened = []
        # Not threatened but must also be removed from threatened squares
        threatened.append(i)
        
        # Diagonal is limted by shortest side
        shortest_side = min(M,N)
        for t in range (0,shortest_side-1):
            threatened.append(i+N+t)
            threatened.append(i+N-t)
            threatened.append(i-N+t)
            threatened.append(i-N-t)
       
        # Remove squares above or below the board
        threatened = [item for item in threatened if item > 0]
        threatened = [item for item in threatened if item <= M*N]

        print(f'{i} : {threatened}')
        avaliable_squares = [x for x in board if x not in threatened]
 
        bishop_values_dict[i]=avaliable_squares
    
    return (bishop_values_dict)

def queen_position_avaliable( M,N, board ):
    """ M is number of rows, N is number of columns, board is list, dict? with avaliable board positions
    """
    i=0
    queen_values_dict = {}
    for i in board:
        # calculate avaliable positions at each queen position by removing unavailable squares.
        avaliable_squares = []
        threatened = []
        # Not threatened but must also be removed from threatened squares
        threatened.append(i)
        
        #Queen just combines bishop and rook rules
        moves = min(M,N) - 1
        for t in range (0,moves):
            threatened.append(i+N+t)
            threatened.append(i+N-t)
            threatened.append(i-N+t)
            threatened.append(i-N-t)

        for t in range (0,N-1):
            threatened.append(i+t)
            threatened.append(i-t)
        for t in range (0,M-1):
            threatened.append(i+t*N)
            threatened.append(i-t*N)
      
        # Remove squares above or below the board
        threatened = [item for item in threatened if item > 0]
        threatened = [item for item in threatened if item <= M*N]

        print(f'{i} : {threatened}')
        avaliable_squares = [x for x in board if x not in threatened]
 
        queen_values_dict[i]=avaliable_squares
    
    return (queen_values_dict)


M=4
N=3
board = create_initial_positions(M,N)
#print(f'Kings: {king_position_avaliable( M,N, board)}')
#print(f'Knights: {knight_position_avaliable( M,N, board)}')
print(f'Rook: {rook_position_avaliable(M,N,board)}')