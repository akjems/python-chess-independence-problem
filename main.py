from create_board import create_initial_positions
from menu import start_menu
from piece_moves import *
from combination_creator import add_piece_to_board

start_data = start_menu()

if start_data:
    M = start_data.get('M')
    N = start_data.get('N')
    
    # I think this is wrong I need my functions to work
    avaliable_positions = create_initial_positions (M,N)
    board = create_initial_positions (M,N)
    # update with kings squares removed
    #avaliable_positions = king_position_avaliable(M,N, avaliable_positions, start_data.get('kings'))

    kings = king_position_avaliable(M,N,board)
    knights = knight_position_avaliable(M,N,board)

    add_piece_to_board(kings, knights)
    


else:
    print('Thank you, come again')