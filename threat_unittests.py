import unittest

import sys
from piece_threats import bishop_threats, trim_threatened, rook_threats

class ThreatsTestCase(unittest.TestCase):

    def test_bishop(self):
        result = trim_threatened(bishop_threats(2,2,1,1,{1}), 4)
        self.assertEqual(result, {1, 4})
    
    def test_rook(self):
        result = trim_threatened(rook_threats(2,2,1,1,{1}), 4)
        self.assertEqual(result, {1,2,3})

    def test_queen(self):
        result = trim_threatened(rook_threats(2,2,1,1,{1}), 4)
        self.assertEqual(result, {1,2,3,4})

    def test_king(self):
        result = trim_threatened(rook_threats(2,2,1,1,{1}), 4)
        self.assertEqual(result, {1,2,3,4})

if __name__ == '__main__':
    unittest.main()

