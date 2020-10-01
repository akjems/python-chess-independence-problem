import unittest

import sys
from squares import squares_avaliable
from combination_creator import add_piece_to_board

class SquaresAvaliableTestCase(unittest.TestCase):
# Pass into test (N,i, current_column, threatened), board_size)
    def test_avaliable_2x2_king(self):
        
        result = squares_avaliable(2,2,"king")
        # from squares avaliable I get a list of frozen sets
        self.assertEqual(result, [(frozenset({1}), frozenset()),(frozenset({2}), frozenset()),(frozenset({3}), frozenset()),(frozenset({4}), frozenset())])

class CombinationsTestCase(unittest.TestCase):
    def test_combinations(self):
        result = add_piece_to_board({1}, {2})
        self.assertEqual(result, [(frozenset({1}), frozenset()),(frozenset({2}), frozenset()),(frozenset({3}), frozenset()),(frozenset({4}), frozenset())])

if __name__ == '__main__':
    unittest.main()

