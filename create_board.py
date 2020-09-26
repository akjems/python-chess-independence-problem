# This class creates and maintains the list of avaliable positions

def create_initial_positions (M,N):
    number_of_squares = M*N
    positions = []
    # Needs to include final square
    for i in range (1,number_of_squares+1,1):
        positions.append(i)
    return (positions)

def dict_initial_board (M,N, board):
    dict_empty_board={}
    for i in board:
        # calculate avaliable positions at each king position by removing unavaiable squares.
        avaliable_squares = []
        threatened = []
        # Not threatened but must also be removed from threatened squares
        threatened.append(i)
        
        avaliable_squares = [x for x in board if x not in threatened]

        empty_board_values[i]=avaliable_squares

        return(dict_empty_board)