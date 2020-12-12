'''
Unit tests for Advent of Code 2020, Day 9.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day09 as pkg

class TestDay09(unittest.TestCase):

    def test_XmasSequence_init(self):
        numbers = (2, 1, 32, 8)
        expected_sums = [(0,1,3),(0,2,34),(0,3,10),(1,2,33),(1,3,9),(2,3,40)]
        xs = pkg.XmasSequence(numbers)
        self.assertEqual(xs.preamble_len, len(numbers))
        self.assertCountEqual(xs.sums, expected_sums)
        self.assertSequenceEqual(xs.prev, numbers)
        self.assertEqual(xs.next_index, len(numbers))
    
    def test_XmasSequence_isValid(self):
        xs = pkg.XmasSequence(range(1,26))
        self.assertTrue(xs.is_valid(26))
        self.assertTrue(xs.is_valid(49))
        self.assertFalse(xs.is_valid(100))
        self.assertFalse(xs.is_valid(50))
    
    def test_XmasSequence_add_next(self):
        numbers = (2, 1, 32, 8)
        xs = pkg.XmasSequence(numbers)
        with self.assertRaises(ValueError):
            xs.add_next(-1)
        next = 40
        xs.add_next(next)
        self.assertEqual(xs.preamble_len, len(numbers))
        expected_sums = ((1,2,33),(1,3,9),(2,3,40),(3,4,48),(2,4,72),(1,4,41))
        self.assertCountEqual(xs.sums, expected_sums)
        self.assertSequenceEqual(xs.prev, numbers[1:] + (next,))
        self.assertEqual(xs.next_index, len(numbers)+1)
    
    def test_next_and_valid(self):
        xs = pkg.XmasSequence((20,)+tuple(range(1,20))+tuple(range(21,26)))
        xs.add_next(45)
        self.assertTrue(xs.is_valid(26))
        self.assertFalse(xs.is_valid(65))
        self.assertTrue(xs.is_valid(64))
        self.assertTrue(xs.is_valid(66))
    
    def test_first_invalid(self):
        self.assertEqual(pkg.first_invalid(pkg.load_numbers('test_input/day09_t1.txt'),5), 127)
    
if __name__ == '__main__':
    unittest.main()
