'''
Unit tests for Advent of Code 2020, Day 24.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day24 as pkg

class TestDay24(unittest.TestCase):
    def test_load_black(self):
        self.assertEqual(len(pkg.load_black('test_input/day24_t1.txt')), 10)
    
    def test_cycle(self):
        black = pkg.load_black('test_input/day24_t1.txt')
        black = pkg.cycle(black)
        self.assertEqual(len(black), 15)
        black = pkg.cycle(black)
        self.assertEqual(len(black), 12)
        black = pkg.cycle(black)
        self.assertEqual(len(black), 25)
        black = pkg.cycle(black)
        self.assertEqual(len(black), 14)
        black = pkg.cycle(black)
        self.assertEqual(len(black), 23)
        black = pkg.cycle(black)
        self.assertEqual(len(black), 28)
        black = pkg.cycle(black)
        self.assertEqual(len(black), 41)
        black = pkg.cycle(black)
        self.assertEqual(len(black), 37)
        black = pkg.cycle(black)
        self.assertEqual(len(black), 49)
        black = pkg.cycle(black)
        self.assertEqual(len(black), 37)
        for _ in range(10): black = pkg.cycle(black)
        self.assertEqual(len(black), 132)
        for _ in range(10): black = pkg.cycle(black)
        self.assertEqual(len(black), 259)
        for _ in range(10): black = pkg.cycle(black)
        self.assertEqual(len(black), 406)
        for _ in range(10): black = pkg.cycle(black)
        self.assertEqual(len(black), 566)
        for _ in range(10): black = pkg.cycle(black)
        self.assertEqual(len(black), 788)
        for _ in range(10): black = pkg.cycle(black)
        self.assertEqual(len(black), 1106)
        for _ in range(10): black = pkg.cycle(black)
        self.assertEqual(len(black), 1373)
        for _ in range(10): black = pkg.cycle(black)
        self.assertEqual(len(black), 1844)
        for _ in range(10): black = pkg.cycle(black)
        self.assertEqual(len(black), 2208)
        
        
if __name__ == '__main__':
    unittest.main()
