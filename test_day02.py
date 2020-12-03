'''
Unit tests for Advent of Code 2020, Day 2.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
from collections import namedtuple
import day02 as pkg

class TestDay02(unittest.TestCase):

    def test_Policy(self):
        p = pkg.Policy('123-4567 Z', None)
        self.assertEqual(p.char, 'Z')
        self.assertEqual(p.max, 4567)
        self.assertEqual(p.min, 123)
        self.assertIsNone(p.check_fn)

    def test_yield_matches(self):
        matches = [c for c in pkg.yield_matches('d', 'abcdedcbadedzd')]
        self.assertEqual(matches, ['d']*5)
        matches = [c for c in pkg.yield_matches('d', 'abcdedcbadedzd'.upper())]
        self.assertEqual(matches, [])
    
    def test_check1(self):
        Policy = namedtuple('Policy', ['min', 'max', 'char'])
        p = Policy(3, 7, 'j')
        self.assertFalse(pkg.check1(p, 'abccba'))
        self.assertFalse(pkg.check1(p, 'abcjjcba'))
        self.assertTrue(pkg.check1(p, 'abcjjjcba'))
        self.assertTrue(pkg.check1(p, 'abcjjjcbjja'))
        self.assertTrue(pkg.check1(p, 'ajbjcjjjcbjja'))
        self.assertFalse(pkg.check1(p, 'jajbjcjjjcbjja'))
        self.assertFalse(pkg.check1(p, 'ajbjcjjjcbjjajjjjjjjjjjjjjjjjjz'))
    
    def test_check2(self):
        Policy = namedtuple('Policy', ['min', 'max', 'char'])
        p = Policy(3, 7, 'j')
        self.assertTrue(pkg.check2(p, 'abjdefghi'))
        self.assertTrue(pkg.check2(p, 'abcdefjhi'))
        self.assertFalse(pkg.check2(p, 'abcdefghi'))
        self.assertFalse(pkg.check2(p, 'abjdefjhi'))

    def test_count_valid(self):
        self.assertEqual(pkg.count_valid('test_input/day02_t1.txt', pkg.check1), 2)
        self.assertEqual(pkg.count_valid('test_input/day02_t1.txt', pkg.check2), 1)

if __name__ == '__main__':
    unittest.main()

