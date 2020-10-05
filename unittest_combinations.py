import unittest

import sys
from squares import squares_available
from combination_creator_2 import add_piece_to_board

class SquaresAvailableTestCase(unittest.TestCase):
# Pass into test (N,i, current_column, threatened), board_size)
    def test_available_2x2_king(self):
        result = squares_available(2,2,"king")
        # from squares available I get a list of frozen sets
        self.assertEqual(result, {(1,):frozenset(),(2,):frozenset(),(3,):frozenset(),(4,): frozenset()})

    def test_available_2x2_bishop(self):
        result = squares_available(2,2,"bishop")
        self.assertEqual(result, {
    (1,):frozenset({2,3}),
    (2,):frozenset({1,4}),
    (3,):frozenset({1,4}),
    (4,):frozenset({2,3})})

    def test_available_2x2_knight(self):
        result = squares_available(2,2,"knight")
        self.assertEqual(result, {
    (1,):frozenset({2,3,4}),
    (2,):frozenset({1,3,4}),
    (3,):frozenset({1,4,2}),
    (4,):frozenset({2,3,1})})

    

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
        self.assertEqual(result, {(2, 1): frozenset({4}), (3, 1): frozenset({4}), (1, 2): frozenset({3}), (4, 2): frozenset({3}), (1, 3): frozenset({2}), (4, 3): frozenset({2}), (2, 4): frozenset({1}), (3, 4): frozenset({1})})

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

if __name__ == '__main__':
    unittest.main()

