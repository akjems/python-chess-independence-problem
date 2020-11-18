"""Functions related to creating the board  """


def column(position,number_of_columns):
    if position%number_of_columns == 0:
    # It's in the last column not 0 column
        current_column = number_of_columns
    else:
        current_column = (position%number_of_columns)
    return current_column


def create_board (M,N):
    number_of_squares = M*N
    positions = []
    # Needs to include final square
    for i in range (1,number_of_squares+1,1):
        positions.append(i)
    return positions
