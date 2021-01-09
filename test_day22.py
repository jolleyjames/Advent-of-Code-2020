'''
Unit tests for Advent of Code 2020, Day 22.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day22 as pkg

class TestDay22(unittest.TestCase):
    def test_load_decks(self):
        p1, p2 = pkg.load_decks('test_input/day22_t1.txt')
        self.assertEqual(p1, [9,2,6,3,1])
        self.assertEqual(p2, [5,8,4,7,10])
    
    def test_play_round(self):
        p1, p2 = pkg.load_decks('test_input/day22_t1.txt')
        pkg.play_round(p1,p2)
        self.assertEqual(p1, [2, 6, 3, 1, 9, 5])
        self.assertEqual(p2, [8, 4, 7, 10])
        pkg.play_round(p1,p2)
        self.assertEqual(p1, [6, 3, 1, 9, 5])
        self.assertEqual(p2, [4, 7, 10, 8, 2])
        pkg.play_round(p1,p2)
        self.assertEqual(p1, [3, 1, 9, 5, 6, 4])
        self.assertEqual(p2, [7, 10, 8, 2])
    
    def test_play_game(self):
        p1, p2 = pkg.load_decks('test_input/day22_t1.txt')
        pkg.play_game(p1,p2)
        self.assertEqual(p1, [])
        self.assertEqual(p2, [3, 2, 10, 6, 8, 5, 9, 4, 7, 1])
    
    def test_score(self):
        winner = [3, 2, 10, 6, 8, 5, 9, 4, 7, 1]
        self.assertEqual(pkg.score(winner), 306)
    
    def test_play_recursive_game_inf(self):
        p1, p2 = pkg.load_decks('test_input/day22_t2.txt')
        self.assertEqual(pkg.play_recursive_game(p1, p2, 99), 99)
    
    def test_play_recursive_game(self):
        p1, p2 = pkg.load_decks('test_input/day22_t1.txt')
        pkg.play_recursive_game(p1, p2)
        self.assertEqual(p1, [])
        self.assertEqual(p2, [7, 5, 6, 2, 4, 1, 10, 8, 9, 3])
        


        
if __name__ == '__main__':
    unittest.main()
