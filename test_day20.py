'''
Unit tests for Advent of Code 2020, Day 20.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day20 as pkg

class TestDay20(unittest.TestCase):
    def test_get_edge_values(self):
        tile = pkg.load_tiles('test_input/day20_t1.txt')[2311]
        exp = [int(s,2) for s in ('11010010','1011001','11100111','111110010')]
        self.assertListEqual(pkg.get_edge_values(tile),exp)
    
    def test_find_corners(self):
        tiles = pkg.load_tiles('test_input/day20_t1.txt')
        corners = pkg.find_corners(pkg.all_edge_values(tiles))
        self.assertCountEqual(corners, [1951,3079,2971,1171])


        
if __name__ == '__main__':
    unittest.main()
