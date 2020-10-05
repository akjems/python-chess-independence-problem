from board import column, create_board
from piece_threats import *

def create_set(size):
    return(set(size))

def update_available_squares(threatened, available_squares):
    """Removes threatened squares from set of available squares"""
    available_squares.difference_update(threatened)
    return(available_squares)

def squares_available(M,N, piece ):
    """ Returns a set of available squares for a piece
        M is number of rows, N is number of columns, board is list
        Calculate available positions at each king position by removing unavailable squares.
    """
    board = create_board(M,N)
    squares_available_set=set()
    squares_available_dict = {}
    i=1
    for i in board:
        available_squares = create_set(board)
        threatened=create_threatened(i)
        occupied=create_occupied(i)
        current_column = column(i,N)

        # Returning from availabe squares is dependent on the piece that is added to the board.
        
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
        available_squares = update_available_squares(threatened, available_squares)
        # key is a tuple of occupied squares. The order is the same the pieces were added in
        
        # NOTE changed from tuple to frozenset
        #squares_available_set.add(frozenset({frozenset({i}),frozenset(available_squares)}))
        position = (i,)
        squares_available_dict[position]=frozenset(available_squares)
        #print(squares_available_dict.get[i])
        
    
    return (squares_available_dict)

def duplicate_piece_cleaner(availabe_with_duplicates):
    list_of_keys = list(availabe_with_duplicates.keys())
    i=0
    while i < len(list_of_keys):
        j = list_of_keys[i][0]
        k = list_of_keys[i][1]
        i+=1
    print(f'j: {j}, k: {k}')
    
    return ()


