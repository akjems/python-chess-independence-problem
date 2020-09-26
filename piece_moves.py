
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

        #threatened = [item for item in threatened if item > 0]
        #threatened = [item for item in threatened if item <= M*N]

        print(f'{i} : {threatened}')
        avaliable_squares = [x for x in board if x not in threatened]
 
        knight_values_dict[i]=avaliable_squares
    
    return (knight_values_dict)

M=2
N=4
board = create_initial_positions(M,N)
print(f'Kings: {king_position_avaliable( M,N, board)}')
print(f'Knights: {knight_position_avaliable( M,N, board)}')