

from squares import *

from combination_creator import *


# combine first set of three, then second set of three, the both sets of three
"""
        M = 6
        N = 9
        kings = 2
        queens = 1
        rooks = 1
        bishops = 1
        knights = 1
"""

start_board_1=squares_avaliable( 6,9, "king" )
new_piece = squares_avaliable( 6,9, "king")
updated_board_1=add_piece_to_board(start_board_1, new_piece)
new_piece = squares_avaliable( 6,9, "queen")
updated_board_1=add_piece_to_board(updated_board_1, new_piece)
print(f'Board 1: {len(updated_board_1)}')


start_board_2=squares_avaliable( 6,9, "rook" )
new_piece = squares_avaliable( 6,9, "bishop")
updated_board_2=add_piece_to_board(start_board_2, new_piece)
new_piece = squares_avaliable( 6,9, "knight")
updated_board_2=add_piece_to_board(updated_board_2, new_piece)
print(f'Board 2: {len(updated_board_2)}')



final_board=add_piece_to_board(updated_board_2, updated_board_1)
print(f'Final Board: {len(final_board)}')




