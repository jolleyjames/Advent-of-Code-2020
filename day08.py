'''
Advent of Code 2020, Day 8.
James Jolley, jim.jolley [at] gmail.com
'''

from typing import Iterable

class Cpu:
    '''
    Implements processor defined in Day 8.
    '''
    def __init__(self, program):
        '''
        Constructor accepts program, either a string to a path, or
        a 2-d iterable of instructions.
        '''
        if type(program) == str:
            program = Cpu.load_program(program)
        if isinstance(program, Iterable):
            self._program = program
        else:
            raise ValueError('program not path or 2-d iterable')

        # set defaults
        self._accumulator = 0
        self._pc = 0

    @property
    def program(self):
        'the list of instructions to be executed'
        return self._program
    
    @property
    def accumulator(self):
        'accumulator register'
        return self._accumulator
    
    @property
    def pc(self):
        'program counter register'
        return self._pc
    
    def step(self):
        'perform the next instruction'
        instr = self.program[self.pc]
        if instr[0] == 'acc':
            self._accumulator += instr[1]
            self._pc += 1
        elif instr[0] == 'jmp':
            self._pc += instr[1]
        elif instr[0] == 'nop':
            self._pc += 1
        else:
            raise ValueError(f'illegal instruction {instr[0]} at pc {self.pc}')
    
    @staticmethod
    def load_program(path):
        '''
        Load program from specified path. Each line will be transformed into
        an iterable: the first item is a string with the instruction, and the
        remaining items are ints.
        '''
        program = []
        with open(path) as file:
            for line in file:
                instr = line.strip().split()
                program.append((instr[0],) + tuple([int(x) for x in instr[1:]]))
        return program
    
def cpu_at_first_repeat_or_end(program):
    '''
    Returns the state of the cpu at the first repeated instruction
    in the given program, 
    '''
    cpu = Cpu(program)
    # instructions executed, by program counter location
    pc_exe = set()
    while cpu.pc not in pc_exe and 0 <= cpu.pc < len(cpu.program):
        pc_exe.add(cpu.pc)
        cpu.step()
    return cpu

def acc_at_first_repeat(program):
    '''
    Returns the value of the accumulator at the first repeated instruction
    in the given program.
    '''
    cpu = cpu_at_first_repeat_or_end(program)
    return cpu.accumulator

def acc_at_end(program):
    '''
    Returns the value of the accumulator using the first modified program
    swapping jmp and nop.
    '''
    program = Cpu.load_program(program)
    last_pc = 0
    while last_pc < len(program):
        if program[last_pc][0] in ('jmp','nop'):
            # swap the instruction
            copy_pgm = list(program)
            new_instr = 'jmp' if program[last_pc][0] == 'nop' else 'nop'
            new_instr = (new_instr,) + tuple(program[last_pc][1:])
            copy_pgm[last_pc] = new_instr
            cpu = cpu_at_first_repeat_or_end(copy_pgm)
            if cpu.pc < 0 or cpu.pc >= len(cpu.program):
                return cpu.accumulator
        last_pc += 1
    # if here then no fixed program was found
    raise ValueError('no fixed program found')

if __name__ == '__main__':
    # part 1
    print(acc_at_first_repeat('input/day08.txt'))
    # part 2
    print(acc_at_end('input/day08.txt'))
    