from create_board import *
from menu import start_menu
from piece_moves import *
from combination_creator import *


start_data = start_menu()
print(start_data)

if start_data:
    M = start_data.get('M')
    N = start_data.get('N')
    kings = start_data.get('kings')
    queens=start_data.get('queens')
    rooks =start_data.get('rooks')
    bishops=start_data.get('bishops')
    knights=start_data.get('knights')
    print(f"Calculating for {kings} kings")
    print(f"Calculating for {queens} queens")
    print(f"Calculating for {rooks} rooks")
    print(f"Calculating for {bishops} bishops")
    print(f"Calculating for {knights} knights")
    print(f"Board size MxN: {M}x{N}\n")


    board = create_board(M,N)

    # setups is a list of tuples of occupied and avaliable squares. Length of setups is answer to challenge
    # setups = [([occupied_squares],[       avaliable_squares           ]           )...]
                     #add key here,    add avaliable_squares here
                # each new piece added, only keep avaliable squares that duplicate

    #TODO Loop over add_piece_to_board until all pieces are added
    i = 1
    while i <= bishops:
        bishop_positions=bishop_position_avaliable(M,N, board)
        i +=1
    i = 1
    while i <= knights:
        knight_positions=knight_position_avaliable(M,N,board)
        i +=1
    
    i = i
    add_piece_to_board(bishop_positions, knight_positions)

else:
    print('Thank you, come again')
