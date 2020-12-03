'''
Advent of Code 2020, Day 2.
James Jolley, jim.jolley [at] gmail.com
'''

class Policy:
    '''
    Defines the minimum and maximum number of times a certain letter must 
    appear within a plaintext password.
    '''

    def __init__(self, policy_str):
        '''
        Define the policy according to a policy string. The policy string
        must follow the following format:
        "m-n c"
        m and n are minimum and maximum, respectively. c is the character.
        '''
        split_policy_str = policy_str.split(' ')
        self._char = split_policy_str[1]
        minmax = split_policy_str[0].split('-')
        self._min, self._max = [int(s) for s in minmax]

    @property
    def char(self):
        return self._char

    @property
    def min(self):
        return self._min

    @property
    def max(self):
        return self._max

    def yield_matches(self, s):
        '''
        Yields each character in s that matches self.char
        '''
        x = 0
        while x < len(s):
            if s[x] == self.char:
                yield self.char
            x += 1
    
    def check(self, passwd):
        '''
        Checks if a plaintext password is valid against the given policy.
        '''
        count = 0
        for match in self.yield_matches(passwd):
            count += 1
            if count > self.max:
                return False
        return count >= self.min

def count_valid(path):
    '''
    Count the number of valid policy/password combinations in the file
    at the specified path.
    '''
    count = 0
    with open(path) as file:
        for line in file:
            line = line.strip()
            policy, passwd = line.split(': ')
            policy = Policy(policy)
            if policy.check(passwd):
                count += 1
    return count

if __name__ == '__main__':
    # part 1
    print(count_valid('input/day02.txt'))
