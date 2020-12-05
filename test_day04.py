'''
Unit tests for Advent of Code 2020, Day 4.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day04 as pkg

class TestDay04(unittest.TestCase):
    def test_load_passports(self):
        self.assertEqual(len(pkg.load_passports('test_input/day04_t1.txt')), 4)
    
    def test_is_valid(self):
        passport = {'a':'A', 'b':'B', 'c':'C', 'd':'D'}
        self.assertTrue(pkg.is_valid(passport, ('b','c','d')))
        self.assertFalse(pkg.is_valid(passport, ('a','e')))
    
    def test_count_valid(self):
        self.assertEqual(pkg.count_valid('test_input/day04_t1.txt'), 2)
        self.assertEqual(pkg.count_valid('test_input/day04_t2.txt', pkg.is_extra_valid), 0)
        self.assertEqual(pkg.count_valid('test_input/day04_t3.txt', pkg.is_extra_valid), 4)        
    
    def test_value_in_range(self):
        self.assertTrue(pkg.value_in_range('123', 3, 123, 900))
        self.assertTrue(pkg.value_in_range('123', 3, 100, 123))
        self.assertFalse(pkg.value_in_range('12E', 3, 100, 123))
        self.assertFalse(pkg.value_in_range('1234', 4, 1235, 2000))
        self.assertFalse(pkg.value_in_range('2001', 4, 1235, 2000))
        self.assertFalse(pkg.value_in_range('123', 4, 123, 900))
        self.assertFalse(pkg.value_in_range('123', 4, 100, 123))
    
    def test_is_extra_valid(self):
        passports = pkg.load_passports('test_input/day04_t2.txt')
        self.assertTrue(all(not pkg.is_extra_valid(p) for p in passports))
        passports = pkg.load_passports('test_input/day04_t3.txt')
        self.assertTrue(all(pkg.is_extra_valid(p) for p in passports))

if __name__ == '__main__':
    unittest.main()
