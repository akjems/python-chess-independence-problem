from board import column, create_board
from piece_threats import *




def create_set(size):
    return(set(size))

def update_avaliable_squares(threatened, avaliable_squares):
    """Removes threatened squares from set of avaliable squares"""
    avaliable_squares.difference_update(threatened)
    return(avaliable_squares)

def squares_avaliable(M,N, piece ):
    """ Returns list of avaliable squares
        M is number of rows, N is number of columns, board is list
        Calculate avaliable positions at each king position by removing unavailable squares.
    """
    board = create_board(M,N)
    squares_avaliable_set=set()
    i=1
    for i in board:
        avaliable_squares = create_set(board)
        threatened=create_threatened(i)
        current_column = column(i,N)

        # This is the only line that changes, so instead single function for all pieces and then this line can be switch.
        
        if piece=="king":
            threatened=king_threats(M,N,i,current_column,threatened)
        elif piece=="queen":
            threatened=queen_threats(M,N,i,current_column,threatened)
        elif piece=="rook":
            threatened=rook_threats(M,N,i,current_column,threatened)
        elif piece=="bishop":
            threatened=bishop_threats(M,N,i,current_column,threatened)
        elif piece=="knight":
            threatened=knight_threats(M,N,i,current_column,threatened)
        else:
            print('all pieces accounted for')

        # Remove squares above or below the board
        threatened=trim_threatened(threatened,M*N)
        
        # remove threatened squares
        avaliable_squares = update_avaliable_squares(threatened, avaliable_squares)
        #print(f'M, N, piece, avaliable squares: {M}, {N}, {piece}, {avaliable_squares}')
        # key is a list of squares with pieces in it
        
        # NOTE changed from tuple to frozenset
        squares_avaliable_set.add(frozenset({frozenset({i}),frozenset(avaliable_squares)}))
    
    return (squares_avaliable_set)
