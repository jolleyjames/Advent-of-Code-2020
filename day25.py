'''
Advent of Code 2020, Day 25.
James Jolley, jim.jolley [at] gmail.com
'''

from operator import mul

DEFAULT_BASE = 7
DEFAULT_P = 20201227

def find_dh_privkey(pubkeys, base=DEFAULT_BASE, p=DEFAULT_P):
    '''
    Find the Diffie-Hellman private key for the two public keys, given the
    known base and prime values.
    '''
    pubkeys = list(pubkeys)
    v,n,power = 1, 0, None
    while len(pubkeys) > 1:
        n += 1
        v *= base
        if v >= p: v %= p
        if v in pubkeys:
            power = n
            pubkeys.remove(v)
    pubkey = pubkeys[0]
    return (pubkey**power) % p

if __name__ == '__main__':
    with open('input/day25.txt') as file:
        pubkeys = [int(line) for line in file.readlines()]
    print(find_dh_privkey(pubkeys))
