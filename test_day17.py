'''
Unit tests for Advent of Code 2020, Day 17.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day17 as pkg

class TestDay17(unittest.TestCase):
    def test_load_cubes(self):
        cubes = pkg.load_cubes('test_input/day17_t1.txt', 90)
        coords = set([(0,2,90),(1,0,90),(1,2,90),(2,1,90),(2,2,90)])
        self.assertSetEqual(cubes, coords)

    def test_load_cubes_4d(self):
        cubes = pkg.load_cubes_4d('test_input/day17_t1.txt', 80, 20)
        coords = set([(80,0,2,20),(80,1,0,20),(80,1,2,20),(80,2,1,20),(80,2,2,20)])
        self.assertSetEqual(cubes, coords)

    def test_next_cube_state(self):
        self.assertFalse(pkg.next_cube_state(True, 1))
        self.assertTrue(pkg.next_cube_state(True, 2))
        self.assertTrue(pkg.next_cube_state(True, 3))
        self.assertFalse(pkg.next_cube_state(True, 4))
        self.assertFalse(pkg.next_cube_state(False, 1))
        self.assertFalse(pkg.next_cube_state(False, 2))
        self.assertTrue(pkg.next_cube_state(False, 3))
        self.assertFalse(pkg.next_cube_state(False, 4))
    
    def test_cycle(self):
        cubes = pkg.load_cubes('test_input/day17_t1.txt')
        self.assertEqual(pkg.count_active_cubes(cubes), 5)
        cubes = pkg.cycle(cubes)
        self.assertEqual(pkg.count_active_cubes(cubes), 11)
        for _ in range(2,7):
            cubes = pkg.cycle(cubes)
        self.assertEqual(pkg.count_active_cubes(cubes), 112)
    
    def test_cycle_noreflect(self):
        cubes = pkg.load_cubes('test_input/day17_t1.txt')
        self.assertEqual(pkg.count_active_cubes(cubes), 5)
        cubes = pkg.cycle(cubes, reflect_z0=False)
        self.assertEqual(pkg.count_active_cubes(cubes, reflect_z0=False), 11)
        for _ in range(2,7):
            cubes = pkg.cycle(cubes, reflect_z0=False)
        self.assertEqual(pkg.count_active_cubes(cubes, reflect_z0=False), 112)

    def test_cycle_4d(self):
        cubes = pkg.load_cubes_4d('test_input/day17_t1.txt')
        self.assertEqual(pkg.count_active_cubes_4d(cubes), 5)
        cubes = pkg.cycle_4d(cubes)
        self.assertEqual(pkg.count_active_cubes_4d(cubes), 29)
        for _ in range(2,7):
            cubes = pkg.cycle_4d(cubes)
        self.assertEqual(pkg.count_active_cubes_4d(cubes), 848)

    
        
if __name__ == '__main__':
    unittest.main()
