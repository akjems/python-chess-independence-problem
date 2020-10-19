import unittest

import sys
from squares import duplicate_piece_cleaner

class CleanDuplicates(unittest.TestCase):


    def test_2x3_2kings(self):
        result = duplicate_piece_cleaner(
            {
                (1, 3): frozenset(), (1, 6): frozenset(), (3, 1): frozenset(), (3, 4): frozenset(), (4, 3): frozenset(), (4, 6): frozenset(), (6, 1): frozenset(), (6, 4): frozenset()
            }
            )

        self.assertEqual(result,{(1, 3): frozenset(), (1, 6): frozenset(), (3, 4): frozenset(), (6, 4): frozenset()})


if __name__ == '__main__':
    unittest.main()

