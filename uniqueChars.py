import sys
import argparse

def argumentSetup():
    parser = argparse.ArgumentParser(description='Determine if a string contains duplicates.')
    parser.add_argument('string', type=str,
                        help='the input string')
    return parser.parse_args()

def checkUniqueChars(string):
    chars = [False]*128
    for x, char in enumerate(string):
        value = ord(char)
        if chars[value] == True:
            return False
        else:
            chars[value] = True
    return True

def main():
    args = argumentSetup()
    if checkUniqueChars(args.string):
        print ("PASS: String contains only unique characters") 
    else: 
        print("FAIL: String contains duplicate characters")

if __name__ == "__main__":
    main()