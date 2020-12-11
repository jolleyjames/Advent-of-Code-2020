'''
Unit tests for Advent of Code 2020, Day 8.
James Jolley, jim.jolley [at] gmail.com
'''

import unittest
import day08 as pkg

class TestDay08(unittest.TestCase):
    
    def test_load_program(self):
        expected = [
            ('nop',0),('acc',1),('jmp',4),('acc',3),('jmp',-3),
            ('acc',-99),('acc',1),('jmp',-4),('acc',6)
        ]
        self.assertListEqual(pkg.Cpu.load_program('test_input/day08_t1.txt'),expected)
    
    def test_Cpu_init(self):
        cpu = pkg.Cpu(())
        self.assertEqual(cpu.accumulator, 0)
        self.assertEqual(cpu.pc, 0)
        self.assertEqual(len(cpu.program), 0)
    
    def test_instructions(self):
        cpu = pkg.Cpu((('acc',4),('acc',12),('nop',20),('jmp',-3)))
        cpu.step()
        cpu.step()
        self.assertEqual(cpu.accumulator, 16)
        self.assertEqual(cpu.pc, 2)
        cpu.step()
        self.assertEqual(cpu.accumulator, 16)
        self.assertEqual(cpu.pc, 3)
        cpu.step()
        self.assertEqual(cpu.accumulator, 16)
        self.assertEqual(cpu.pc, 0)
    
    def test_acc_at_first_repeat(self):
        self.assertEqual(pkg.acc_at_first_repeat('test_input/day08_t1.txt'), 5)
    
    def test_acc_at_end(self):
        self.assertEqual(pkg.acc_at_end('test_input/day08_t1.txt'), 8)
        
if __name__ == '__main__':
    unittest.main()
