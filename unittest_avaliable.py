import unittest

import sys
from squares import squares_avaliable

class SquaresAvaliableTestCase(unittest.TestCase):
# Pass into test (N,i, current_column, threatened), board_size)
    def test_avaliable_2x2_king(self):
        
        result = squares_avaliable(2,2,"king")
        self.assertEqual(result, [(frozenset({1}), frozenset()),(frozenset({2}), frozenset()),(frozenset({3}), frozenset()),(frozenset({4}), frozenset())])

if __name__ == '__main__':
    unittest.main()

