import unittest

import sys
from piece_threats import bishop_threats, trim_threatened, rook_threats, king_threats, queen_threats, knight_threats

class KingThreatsTestCase(unittest.TestCase):
# Pass into test (M,N,i, current_column, threatened), board_size)
    def test_king_2x2_1(self):        
        result = trim_threatened(king_threats(2,1,1,{1}), 4)
        self.assertEqual(result, {1,2,3,4})

    def test_king_3x3_1(self):
        result = trim_threatened(king_threats(3,1,1,{1}), 9)
        self.assertEqual(result, {1,2,4,5})

    def test_king_3x3_5(self):
        result = trim_threatened(king_threats(3,5,2,{5}), 9)
        self.assertEqual(result, {1,2,3,4,5,6,7,8,9})

class QueenThreatsTestCase(unittest.TestCase):

    def test_queen_3x3_1(self):
        i=1
        result = trim_threatened(queen_threats(3,3,i,1,{i}), 9)
        self.assertEqual(result, {1,2,3,4,5,7,9})

    def test_queen_2x5_1(self):
        i=1
        result = trim_threatened(queen_threats(2,5,i,1,{i}), 10)
        self.assertEqual(result, {1,2,3,4,5,6})

    def test_queen_3x3_5(self):
        i=5
        result = trim_threatened(queen_threats(3,3,i,2,{i}), 9)
        self.assertEqual(result, {1,2,3,4,4,5,6,7,8,9})

class RookThreatsTestCase(unittest.TestCase):
    
    def test_rook_4x4_5(self):
        i=5
        result = trim_threatened(rook_threats(4,4,i,1,{i}), 16)
        self.assertEqual(result, {1,6,7,8,9})

    def test_rook_8x1_1(self):
        i=1
        result = trim_threatened(rook_threats(8,1,i,1,{i}), 8)
        self.assertEqual(result, {1,2,3,,4,5,6,7,8})

    def test_rook_1x8_1(self):
        result = trim_threatened(rook_threats(1,8,i,1,{i}), 8)
        self.assertEqual(result, {1,2,3,5,6,7,8})

class BishopThreatsTestCase(unittest.TestCase):

    def test_bishop_3x3_5(self):
        i=5
        result = trim_threatened(bishop_threats(3,3,i,2,{i}), 9)
        self.assertEqual(result, {1, 3,5,7,9})
"""
    def test_bishop_8x3_9(self):
        i=9
        result = trim_threatened(bishop_threats(8,3,i,1,{i}), 24)
        self.assertEqual(result, {1, 4})
"""
    
class KnightThreatsTestCase(unittest.TestCase):

    def test_knight_2x2_3(self):
        i=3
        result = trim_threatened(knight_threats(2,2,i,1,{i}), 3)
        self.assertEqual(result, {3})

    def test_knight_8x8_32(self):
        i=32
        result = trim_threatened(knight_threats(8,8,32,8,{i}), 64)
        self.assertEqual(result, {1})

    def test_knight_4x4_16(self):
        i=16
        result = trim_threatened(knight_threats(4,4,i,4,{i}), 16)
        self.assertEqual(result, {1})



if __name__ == '__main__':
    unittest.main()

