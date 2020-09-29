from edge_checker import column
from piece_threats import *




def create_set(size):
    return(set(size))

def update_avaliable_squares(threatened, avaliable_squares):
    """Removes threatened squares from set of avaliable squares"""
    avaliable_squares.difference_update(threatened)
    return(avaliable_squares)

def squares_avaliable( M,N, board, piece ):
    """ M is number of rows, N is number of columns, board is list
        Calculate avaliable positions at each king position by removing unavailable squares.
    """
    squares_avaliable_list=[]
    i=1
    for i in board:
        avaliable_squares = create_set(board)
        threatened=create_threatened(i)
        current_column = column(i,N)

        # This is the only line that changes, so instead single function for all pieces and then this line can be switch.
        
        if piece=="king":
            threatened=king_threats(N,i,current_column,threatened)
        elif piece=="queen":
            threatened=king_threats(N,i,current_column,threatened)
        elif piece=="rook":
            threatened=king_threats(N,i,current_column,threatened)
        elif piece=="bishop":
            threatened=king_threats(N,i,current_column,threatened)
        elif piece=="knight":
            threatened=king_threats(N,i,current_column,threatened)
        else:
            print('all pieces accounted for')

        # Remove squares above or below the board
        threatened=trim_threatened(threatened,M*N)
        
        # remove threatened squares
        avaliable_squares = update_avaliable_squares(threatened, avaliable_squares)

        # key is a list of squares with pieces in it
        squares_avaliable_list.append((frozenset({i}),frozenset(avaliable_squares)))
    
    return (squares_avaliable_list)
