import unittest

from squares import squares_available
from combination_creator import add_piece_to_board

class SquaresAvailableTestCase(unittest.TestCase):
# Pass into test (N,i, current_column, threatened), board_size)
    def test_available_2x2_king(self):
        result = squares_available(2,2,"king")
        # from squares available I get a list of frozen sets
        self.assertEqual(
            result, {
                (1,):frozenset(),
                (2,):frozenset(),
                (3,):frozenset(),
                (4,): frozenset()
            }
        )

    def test_available_2x2_bishop(self):
        result = squares_available(2,2,"bishop")
        self.assertEqual(
            result, {
                (1,):frozenset({2,3}),
                (2,):frozenset({1,4}),
                (3,):frozenset({1,4}),
                (4,):frozenset({2,3})
            }
        )

    def test_available_2x2_knight(self):
        result = squares_available(2,2,"knight")
        self.assertEqual(
            result, {
                (1,):frozenset({2,3,4}),
                (2,):frozenset({1,3,4}),
                (3,):frozenset({1,4,2}),
                (4,):frozenset({2,3,1})
            }
        )


class CombinationsTestCase(unittest.TestCase):
    def test_combinations_2x2_bishop_knight(self):
        result = add_piece_to_board(
            {
                (1,):frozenset({2,3}),
                (2,):frozenset({1,4}),
                (3,):frozenset({1,4}),
                (4,):frozenset({2,3})
            },
            {
                (1,):frozenset({2,3,4}),
                (2,):frozenset({1,3,4}),
                (3,):frozenset({1,4,2}),
                (4,):frozenset({2,3,1})
            }
        )
        self.assertEqual(
            result, {
                (2, 1): frozenset({4}),
                (3, 1): frozenset({4}),
                (1, 2): frozenset({3}),
                (4, 2): frozenset({3}),
                (1, 3): frozenset({2}),
                (4, 3): frozenset({2}),
                (2, 4): frozenset({1}),
                (3, 4): frozenset({1})
            }
        )

    def test_combinations_2x2_bishop_knight_knight(self):
        result = add_piece_to_board(
            {
                (2, 1): frozenset({4}),
                (3, 1): frozenset({4}),
                (1, 2): frozenset({3}),
                (4, 2): frozenset({3}),
                (1, 3): frozenset({2}),
                (4, 3): frozenset({2}),
                (2, 4): frozenset({1}),
                (3, 4): frozenset({1})
            },
            {

                (1,):frozenset({2,3,4}),
                (2,):frozenset({1,3,4}),
                (3,):frozenset({1,4,2}),
                (4,):frozenset({2,3,1})
            }
        )

        self.assertEqual(result, 
        {
            (2, 1, 4): frozenset(), 
            (3, 1, 4): frozenset(), 
            (1, 2, 3): frozenset(), 
            (4, 2, 3): frozenset(), 
            (1, 3, 2): frozenset(), 
            (4, 3, 2): frozenset(), 
            (2, 4, 1): frozenset(), 
            (3, 4, 1): frozenset()
            }
        )
    
    def test_combinations_3x3_king_king(self):
        result = add_piece_to_board(
            {
               (1,): frozenset({3, 6, 7, 8, 9}),
                (2,): frozenset({8, 9, 7}),
                (3,): frozenset({1, 4, 7, 8, 9}),
                (4,): frozenset({9, 3, 6}),
                (5,): frozenset(),
                (6,): frozenset({1, 4, 7}),
                (7,): frozenset({1, 2, 3, 6, 9}),
                (8,): frozenset({1, 2, 3}),
                (9,): frozenset({1, 2, 3, 4, 7})
            },
            {
                (1,): frozenset({3, 6, 7, 8, 9}),
                (2,): frozenset({8, 9, 7}),
                (3,): frozenset({1, 4, 7, 8, 9}),
                (4,): frozenset({9, 3, 6}),
                (5,): frozenset(), (6,): frozenset({1, 4, 7}),
                (7,): frozenset({1, 2, 3, 6, 9}),
                (8,): frozenset({1, 2, 3}),
                (9,): frozenset({1, 2, 3, 4, 7})
            }
        )

        self.assertEqual(result, 
            {
                (1, 3): frozenset({8, 9, 7}),
                (1, 6): frozenset({7}),
                (1, 7): frozenset({9, 3, 6}),
                (1, 8): frozenset({3}),
                (1, 9): frozenset({3, 7}),
                (2, 7): frozenset({9}),
                (2, 8): frozenset(),
                (2, 9): frozenset({7}),
                (3, 1): frozenset({8, 9, 7}),
                (3, 4): frozenset({9}),
                (3, 7): frozenset({1, 9}),
                (3, 8): frozenset({1}),
                (3, 9): frozenset({1, 4, 7}),
                (4, 3): frozenset({9}),
                (4, 6): frozenset(),
                (4, 9): frozenset({3}),
                (6, 1): frozenset({7}),
                (6, 4): frozenset(),
                (6, 7): frozenset({1}),
                (7, 1): frozenset({9, 3, 6}),
                (7, 2): frozenset({9}),
                (7, 3): frozenset({1, 9}),
                (7, 6): frozenset({1}),
                (7, 9): frozenset({1, 2, 3}),
                (8, 1): frozenset({3}),
                (8, 2): frozenset(),
                (8, 3): frozenset({1}),
                (9, 1): frozenset({3, 7}),
                (9, 2): frozenset({7}),
                (9, 3): frozenset({1, 4, 7}),
                (9, 4): frozenset({3}),
                (9, 7): frozenset({1, 2, 3})
            }
        
        )
   
    def test_combinations_3x3_2xking_rook(self):
        result = add_piece_to_board(
            {
                (1, 3): frozenset({8, 9, 7}),
                (1, 6): frozenset({7}),
                (1, 7): frozenset({9, 3, 6}),
                (1, 8): frozenset({3}),
                (1, 9): frozenset({3, 7}),
                (2, 7): frozenset({9}),
                (2, 8): frozenset(),
                (2, 9): frozenset({7}),
                (3, 1): frozenset({8, 9, 7}),
                (3, 4): frozenset({9}),
                (3, 7): frozenset({1, 9}),
                (3, 8): frozenset({1}),
                (3, 9): frozenset({1, 4, 7}),
                (4, 3): frozenset({9}),
                (4, 6): frozenset(),
                (4, 9): frozenset({3}),
                (6, 1): frozenset({7}),
                (6, 4): frozenset(),
                (6, 7): frozenset({1}),
                (7, 1): frozenset({9, 3, 6}),
                (7, 2): frozenset({9}),
                (7, 3): frozenset({1, 9}),
                (7, 6): frozenset({1}),
                (7, 9): frozenset({1, 2, 3}),
                (8, 1): frozenset({3}),
                (8, 2): frozenset(),
                (8, 3): frozenset({1}),
                (9, 1): frozenset({3, 7}),
                (9, 2): frozenset({7}),
                (9, 3): frozenset({1, 4, 7}),
                (9, 4): frozenset({3}),
                (9, 7): frozenset({1, 2, 3})
            },
            {
               (1,): frozenset({8, 9, 5, 6}),
                (2,): frozenset({9, 4, 6, 7}),
                (3,): frozenset({8, 4, 5, 7}),
                (4,): frozenset({8, 9, 2, 3}),
                (5,): frozenset({1, 3, 9, 7}),
                (6,): frozenset({8, 1, 2, 7}),
                (7,): frozenset({2, 3, 5, 6}),
                (8,): frozenset({1, 3, 4, 6}),
                (9,): frozenset({1, 2, 4, 5})
            }
        )

        self.assertEqual(result, {})


if __name__ == '__main__':
    unittest.main()
