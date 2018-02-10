import argparse

def arg_setup():
    parser = argparse.ArgumentParser(description='Reverse an input string.')
    parser.add_argument('s', type=str,
                        help='the input string to be reversed')
    return parser.parse_args()

'''
First solution:
Input: string
Return: input string, reversed
Efficiency: 
    O(n)
    Iterates through the original string once, 
    performing constant time operations
'''
def reverse_string_orig(str):
    rev_list = []
    length = len(str)
    for i in range(length):
        rev_list.append(str[length-1-i])
    rev_str = "".join(rev_list)
    return rev_str

'''
Second solution, more readable, with same input, return, and efficiency
'''
def reverse_str(s):
    rev_list = []
    i = len(s)
    while i:
        i -= 1
        rev_list.append(s[i])
    rev_str = "".join(rev_list)
    return rev_str

def main():
    args = arg_setup()
    print(reverse_str(args.s))

if __name__ == "__main__":
    main()
