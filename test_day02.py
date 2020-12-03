'''
Unit tests for Advent of Code 2020, Day 2.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day02 as pkg

class TestDay02(unittest.TestCase):

    def test_Policy(self):
        p = pkg.Policy('123-4567 Z')
        self.assertEqual(p.char, 'Z')
        self.assertEqual(p.max, 4567)
        self.assertEqual(p.min, 123)

    def test_yield_matches(self):
        p = pkg.Policy('1-2 d')
        matches = [c for c in p.yield_matches('abcdedcbadedzd')]
        self.assertEqual(matches, ['d']*5)
        matches = [c for c in p.yield_matches('abcdedcbadedzd'.upper())]
        self.assertEqual(matches, [])
    
    def test_check(self):
        p = pkg.Policy('3-7 j')
        self.assertFalse(p.check('abccba'))
        self.assertFalse(p.check('abcjjcba'))
        self.assertTrue(p.check('abcjjjcba'))
        self.assertTrue(p.check('abcjjjcbjja'))
        self.assertTrue(p.check('ajbjcjjjcbjja'))
        self.assertFalse(p.check('jajbjcjjjcbjja'))
        self.assertFalse(p.check('ajbjcjjjcbjjajjjjjjjjjjjjjjjjjz'))
    
    def test_count_valid(self):
        self.assertEqual(pkg.count_valid('test_input/day02_t1.txt'), 2)

if __name__ == '__main__':
    unittest.main()

