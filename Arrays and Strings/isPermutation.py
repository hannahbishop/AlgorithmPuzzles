import argparse

def arg_setup():
    parser = argparse.ArgumentParser(description='Determine if 2 strings are permutations of each other')
    parser.add_argument('s1', type=str,
                        help='the first input string')
    parser.add_argument('s2', type=str,
                        help='the second input string')
    return parser.parse_args()
'''
def is_permutation_first_draft(s1, s2):
    char_count = {}
    is_permutation = True
    if len(s1) != len(s2):
        is_permutation = False
    else:
        for c in s1:
            if c in char_count:
                char_count[c] = char_count[c] + 1
            else:
                char_count[c] = 1
        for c in s2:
            print(char_count)
            if c in char_count:
                if char_count[c] > 0:
                    char_count[c] = char_count[c] - 1
                else:
                    is_permutation = False
    return is_permutation
'''

def is_permutation(s1, s2):
    '''
    Input: 
        string s1
        string s2
    Return: 
        True if s1 and s2 are permutations of each other,
        False if s1 and s2 are not permutations of each other
    Time Efficiency: 
        O(n)
        Iterates through both strings once, 
        performing constant time operations at each iteration
    '''
    char_count = [0] * 256
    is_permutation = True
    if len(s1) != len(s2):
        is_permutation = False
    else:
        for c in s1:
            char_count[ord(c)] += 1
        for c in s2:
            if char_count[ord(c)]:
                char_count[ord(c)] -= 1
            else:
                is_permutation = False
    return is_permutation

def main():
    args = arg_setup()
    print(is_permutation(args.s1, args.s2))

if __name__ == "__main__":
    main()