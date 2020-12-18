'''
Unit tests for Advent of Code 2020, Day 11.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day11 as pkg

class TestDay11(unittest.TestCase):
    def test_cycle(self):
        seats = pkg.load_seats('test_input/day11_t1.txt')
        pkg.cycle(seats)
        self.assertDictEqual(seats, pkg.load_seats('test_input/day11_t2.txt'))
        pkg.cycle(seats)
        self.assertDictEqual(seats, pkg.load_seats('test_input/day11_t3.txt'))
        pkg.cycle(seats)
        self.assertDictEqual(seats, pkg.load_seats('test_input/day11_t4.txt'))
        pkg.cycle(seats)
        self.assertDictEqual(seats, pkg.load_seats('test_input/day11_t5.txt'))
        pkg.cycle(seats)
        self.assertDictEqual(seats, pkg.load_seats('test_input/day11_t6.txt'))
    
    def test_stabilize(self):
        seats = pkg.load_seats('test_input/day11_t1.txt')
        pkg.stabilize(seats)
        self.assertDictEqual(seats, pkg.load_seats('test_input/day11_t6.txt'))
        self.assertEqual(pkg.count_all_occ(seats), 37)
    
    def test_get_visible(self):
        seats = pkg.load_seats('test_input/day11_t1.txt')
        pkg.cycle(seats, pkg.occ_visible, 5)
        self.assertDictEqual(seats, pkg.load_seats('test_input/day11_ta2.txt'))
        pkg.cycle(seats, pkg.occ_visible, 5)
        self.assertDictEqual(seats, pkg.load_seats('test_input/day11_ta3.txt'))
        pkg.cycle(seats, pkg.occ_visible, 5)
        self.assertDictEqual(seats, pkg.load_seats('test_input/day11_ta4.txt'))
        pkg.cycle(seats, pkg.occ_visible, 5)
        self.assertDictEqual(seats, pkg.load_seats('test_input/day11_ta5.txt'))
        pkg.cycle(seats, pkg.occ_visible, 5)
        self.assertDictEqual(seats, pkg.load_seats('test_input/day11_ta6.txt'))
        pkg.cycle(seats, pkg.occ_visible, 5)
        self.assertDictEqual(seats, pkg.load_seats('test_input/day11_ta7.txt'))
        seats = pkg.load_seats('test_input/day11_t1.txt')
        pkg.stabilize(seats, pkg.occ_visible, 5)
        self.assertDictEqual(seats, pkg.load_seats('test_input/day11_ta7.txt'))
        self.assertEqual(pkg.count_all_occ(seats), 26)


if __name__ == '__main__':
    unittest.main()
