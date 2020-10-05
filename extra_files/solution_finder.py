

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
# There hahs to be a mathematical shortcut to solve this

board_options_1=squares_available( 6,9, "queen" )
new_piece = squares_available( 6,9, "rook")
board_options_1=add_piece_to_board(board_options_1, new_piece)
print(f'B1 completed: {len(board_options_1)}')


board_options_2 = squares_available( 6,9, "bishop")
board_options_2=add_piece_to_board(board_options_2, new_piece)
new_piece = squares_available( 6,9, "king")
board_options_2=add_piece_to_board(board_options_2, new_piece)
print(f'B2 completed: {len(board_options_2)}')


board_options_3 = squares_available( 6,9, "bishop")
new_piece = squares_available( 6,9, "knight")
board_options_3=add_piece_to_board(board_options_3, new_piece)
print(f'B3 completed: {len(board_options_3)}')


board_options_4 = add_piece_to_board(board_options_3, board_options_1)
print(f'B1+B3 completed: {len(board_options_4)}')

board_options_5 = add_piece_to_board(board_options_3, board_options_4)
print(f'B3+B4 completed: {len(board_options_5)}')

"""
start_board_3=squares_available( 6,9, "rook" )
new_piece = squares_available( 6,9, "queen")
updated_board_3=add_piece_to_board(start_board_3, new_piece)
new_piece = squares_available( 6,9, "bishop")
updated_board_3=add_piece_to_board(updated_board_3, new_piece)
print(f'Board 3: R, Q, B: {len(updated_board_3)}')
"""

#final_board=add_piece_to_board(board_options_2, board_options_1)
#print(f'Final Board: {len(final_board)}')




