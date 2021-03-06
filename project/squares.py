from board import column, create_board
from piece_threats import *


def create_set(size):
    return set(size)


def update_available_squares(threatened, available_squares):
    """
    Removes threatened squares from set of available squares
    """
    available_squares.difference_update(threatened)
    return available_squares


def squares_available(m, n, piece):
    """
    Returns a set of available squares for a piece
    M is number of rows, N is number of columns, board is list
    Calculate available positions at each king position by removing unavailable
    squares.
    """
    board = create_board(m, n)
    squares_available_dict = {}
    i=1
    for i in board:
        available_squares = create_set(board)
        threatened=create_threatened(i)
        current_column = column(i,n)
        # Returning from avaliabe squares is dependent on the piece that
        # is added to the board.
        if piece=="king":
            threatened=king_threats(m, n, i, current_column,threatened)
        elif piece=="queen":
            threatened=queen_threats(m, n, i , current_column,threatened)
        elif piece=="rook":
            threatened=rook_threats(m, n, i, current_column,threatened)
        elif piece=="bishop":
            threatened=bishop_threats(m, n, i, current_column,threatened)
        elif piece=="knight":
            threatened=knight_threats(m, n, i, current_column,threatened)
        else:
            print('all pieces accounted for')
        # Remove squares above or below the board
        threatened=trim_threatened(threatened, m*n)

        # remove threatened squares
        available_squares = \
            update_available_squares(threatened, available_squares)
        # key is a tuple of occupied squares.
        # The order is the same the pieces were added in
        position = (i,)
        squares_available_dict[position] = frozenset(available_squares)
    return squares_available_dict
