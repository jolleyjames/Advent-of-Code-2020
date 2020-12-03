'''
Advent of Code 2020, Day 2.
James Jolley, jim.jolley [at] gmail.com
'''

def yield_matches(c, s):
    '''
    Yields each character c that appears in string s
    '''
    x = 0
    while x < len(s):
        if s[x] == c:
            yield c
        x += 1

def check1(policy, passwd):
    '''
    Checks if a plaintext password is valid against the given policy.
    The password is valid if the character policy_self.char appears at 
    least policy_self.min times, but no more than policy_self.max times.
    '''
    count = 0
    for match in yield_matches(policy.char, passwd):
        count += 1
        if count > policy.max:
            return False
    return count >= policy.min

class Policy:
    '''
    Defines the minimum and maximum number of times a certain letter must 
    appear within a plaintext password.
    '''

    def __init__(self, policy_str, check_fn):
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
        self._check_fn = check_fn

    @property
    def char(self):
        return self._char

    @property
    def min(self):
        return self._min

    @property
    def max(self):
        return self._max
    
    @property
    def check_fn(self):
        return self._check_fn
    
    def check(self, passwd):
        '''
        Check the password using the specified check function.
        '''
        return self.check_fn(self, passwd)
    
def count_valid(path, check):
    '''
    Count the number of valid policy/password combinations in the file
    at the specified path, using the specified check function.
    '''
    count = 0
    with open(path) as file:
        for line in file:
            line = line.strip()
            policy, passwd = line.split(': ')
            policy = Policy(policy, check)
            if policy.check(passwd):
                count += 1
    return count

if __name__ == '__main__':
    # part 1
    print(count_valid('input/day02.txt', check1))
