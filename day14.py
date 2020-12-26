'''
Advent of Code 2020, Day 14.
James Jolley, jim.jolley [at] gmail.com
'''

def parse_mask(s):
    '''
    Parse a "mask" instruction into a 3-tuple containing the string "mask",
    an and-mask which can be used to force bits to 0, and an or-mask which
    can be used to force bits to 1.
    '''
    bits = s.strip().split(' = ')[1]
    and_mask = int(''.join(['1' if c != '0' else '0' for c in bits]), 2)
    or_mask = int(''.join(['0' if c != '1' else '1' for c in bits]), 2)
    return ('mask', and_mask, or_mask)

def parse_write(s):
    '''
    Parse a "mem" instruction into a 3-tuple containing the string "mem",
    the memory address to be written to, and the value to be written before
    masking.
    '''
    s = s.strip().split(' = ')
    val = int(s[1])
    addr = int(s[0][4:-1])
    return ('mem', addr, val)

def run_program(path):
    '''
    Load the instructions at the path, and run the program on an emulated
    36-bit addressable memory block.
    '''
    with open(path) as file:
        program = [parse_mask(line) if line[:4] == 'mask' else parse_write(line) for line in file.readlines()]
    mem = {}
    and_mask, or_mask = None, None
    for instr in program:
        if instr[0] == 'mask':
            _, and_mask, or_mask = instr
        elif instr[0] == 'mem':
            mem[instr[1]] = instr[2] & and_mask | or_mask
        else:
            raise ValueError(f'undefined instruction {instr[0]}')
    return mem

def sum_mem(mem):
    '''
    Return the sum of all values in memory. Assume values not specified in
    the dict are 0.
    '''
    return sum(mem.values())

def parse_mask_v2(s):
    '''
    Returns just the bitmap string from an instruction beginning with
    "mask = ".
    '''
    return s.strip().split(' = ')[1]

def run_program_v2(path):
    '''
    Load the instructions at the path, and run the program on an emulated
    **version 2** controller chip with a 36-bit addressable memory block.
    '''
    with open(path) as file:
        program = [parse_mask_v2(line) if line[:4] == 'mask' else parse_write(line) for line in file.readlines()]
    mem = {}
    mask, ones, floating_powers = [None]*3
    for instr in program:
        if type(instr) == str:
            mask = instr
            ones = int(''.join(['1' if c == '1' else '0' for c in mask]),2)
            floating_powers = []
            for i in range(36):
                if mask[-i-1] == 'X':
                    floating_powers.append(i)
        elif instr[0] == 'mem':
            base_addr, value = instr[1:]
            base_addr |= ones
            for p in floating_powers:
                if (base_addr // (2**p)) % 2 == 1:
                    base_addr -= (2**p)
            addrs = [base_addr]
            for p in floating_powers:
                addrs.extend([a | (2**p) for a in addrs])
            for a in addrs:
                mem[a] = value
        else:
            raise ValueError(f'undefined instruction {instr[0]}')
    return mem

if __name__ == '__main__':
    # part 1
    print(sum_mem(run_program('input/day14.txt')))
    # part 2
    print(sum_mem(run_program_v2('input/day14.txt')))
    