from board import *
from menu import start_menu
from squares import *

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

    number_of_pieces = kings+queens+rooks+bishops+knights

    board = create_board(M,N)
  
    pieces=0  
    print(f'number of pieces: {number_of_pieces}')
    while pieces<number_of_pieces:
        pieces+=1
        # First run start with any that has more than one
        # TODO make this better
        # TODO Add predication of how long calculation will take
        if pieces==1:
            if kings > 0:
                piece="king"
                start_board=squares_avaliable( M,N, board, piece )
                kings = kings -1
            elif queens > 0:
                piece="queen"
                start_board=squares_avaliable( M,N, board, piece )
                queens = queens - 1
            elif rooks > 0:
                piece="rook"
                start_board=squares_avaliable( M,N, board, piece )
                rooks = rooks - 1
            elif bishops > 0:
                piece="bishop"
                start_board=squares_avaliable( M,N, board, piece )
                bishops = bishops - 1
            elif knights > 0:
                piece="knight"
                start_board=squares_avaliable( M,N, board, piece )
                knights= knights-1
        #print(f'start_board: {start_board}\n')
        print(f'Number of Combinations with {pieces} pieces: {len(start_board)}')
        

        if kings > 0:
            piece="king"
            new_piece = squares_avaliable( M,N, board, piece )
            kings = kings -1
            updated_board=add_piece_to_board(start_board, new_piece)
            start_board=updated_board
        elif queens > 0:
            piece="queen"
            new_piece=squares_avaliable( M,N, board, piece )
            queens = queens - 1
            updated_board=add_piece_to_board(start_board, new_piece)
            start_board=updated_board
        elif rooks > 0:
            piece="rook"
            new_piece=squares_avaliable( M,N, board, piece )
            rooks = rooks - 1
            updated_board=add_piece_to_board(start_board, new_piece)
            start_board=updated_board
        elif bishops > 0:
            piece="bishop"
            new_piece=squares_avaliable( M,N, board, piece )
            bishops = bishops - 1
            updated_board=add_piece_to_board(start_board, new_piece)
            start_board=updated_board
        elif knights > 0:
            piece="knight"
            new_piece=squares_avaliable( M,N, board, piece )
            knights= knights-1
            updated_board=add_piece_to_board(start_board, new_piece)
            start_board=updated_board
        else:
            None
 

    print(f'Number of Combinations FINAL: {len(start_board)}')

else:
    print('Thank you, come again')
