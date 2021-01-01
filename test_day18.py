'''
Unit tests for Advent of Code 2020, Day 18.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day18 as pkg

class TestDay18(unittest.TestCase):
    def test_parse_expression(self):
        n = pkg.parse_expression('1 + 2 * 3 + 4 * 5 + 6')
        self.assertEqual(n.evaluate(), 71)
        n = pkg.parse_expression('1 + (2 * 3) + (4 * (5 + 6))')
        self.assertEqual(n.evaluate(), 51)
        n = pkg.parse_expression('2 * 3 + (4 * 5)')
        self.assertEqual(n.evaluate(), 26)
        n = pkg.parse_expression('5 + (8 * 3 + 9 + 3 * 4 * 3)')
        self.assertEqual(n.evaluate(), 437)
        n = pkg.parse_expression('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')
        self.assertEqual(n.evaluate(), 12240)
        n = pkg.parse_expression('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')
        self.assertEqual(n.evaluate(), 13632)

    def test_parse_expression_advanced(self):
        n = pkg.parse_expression('1 + 2 * 3 + 4 * 5 + 6', True)
        self.assertEqual(n.evaluate(), 231)
        n = pkg.parse_expression('1 + (2 * 3) + (4 * (5 + 6))', True)
        self.assertEqual(n.evaluate(), 51)
        n = pkg.parse_expression('2 * 3 + (4 * 5)', True)
        self.assertEqual(n.evaluate(), 46)
        n = pkg.parse_expression('5 + (8 * 3 + 9 + 3 * 4 * 3)', True)
        self.assertEqual(n.evaluate(), 1445)
        n = pkg.parse_expression('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', True)
        self.assertEqual(n.evaluate(), 669060)
        n = pkg.parse_expression('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', True)
        self.assertEqual(n.evaluate(), 23340)

        
if __name__ == '__main__':
    unittest.main()
