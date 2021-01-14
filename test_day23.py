'''
Unit tests for Advent of Code 2020, Day 23.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day23 as pkg

class TestDay23(unittest.TestCase):
    def test_input_to_list(self):
        s = '9630'
        self.assertListEqual(pkg.input_to_list(s), list(range(9,-1,-3)))
    
    def test_move_to_destination(self):
        cups = pkg.input_to_list('389125467')
        pkg.move_to_destination(cups)
        self.assertListEqual(cups, [2, 8,  9,  1,  5,  4,  6,  7, 3])
        pkg.move_to_destination(cups)
        self.assertListEqual(cups, [5, 4,  6,  7,  8,  9,  1, 3, 2])
        pkg.move_to_destination(cups)
        self.assertListEqual(cups, [8, 9,  1,  3,  4,  6, 7, 2, 5])
        for _ in range(7):
            pkg.move_to_destination(cups)
        self.assertListEqual(cups, [8, 3,  7,  4,  1,  9,  2,  6, 5])
    
    def test_cups_after_1(self):
        self.assertEqual(pkg.cups_after_1([1, 2, 3, 4, 5]), '2345')
        self.assertEqual(pkg.cups_after_1([5, 4, 3, 2, 1]), '5432')
        self.assertEqual(pkg.cups_after_1([0,2,3,4,5,6,7,1,8,9]), '890234567')
        cups = pkg.input_to_list('389125467')
        for _ in range(10):
            pkg.move_to_destination(cups)
        self.assertEqual(pkg.cups_after_1(cups), '92658374')
        for _ in range(90):
            pkg.move_to_destination(cups)
        self.assertEqual(pkg.cups_after_1(cups), '67384529')
        



        
if __name__ == '__main__':
    unittest.main()
