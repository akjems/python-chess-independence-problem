# These functions create and maintain the list of avaliable positions for each piece added to the board

def create_board (M,N):
    number_of_squares = M*N
    positions = []
    # Needs to include final square
    for i in range (1,number_of_squares+1,1):
        positions.append(i)
    return (positions)

def create_initial_positions(M,N, board):
    dict_empty_board={}
    for i in board:
        # calculate avaliable positions at each king position by removing unavailable squares.
        avaliable_squares = board
        # Not threatened but must also be removed from threatened squares

        dict_empty_board[i]=avaliable_squares


    return(dict_empty_board)