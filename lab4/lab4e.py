#!/usr/bin/env python3
# Author ID: 103021226

def is_digits(sobj):
    # place code here - loop through each character in sobj 
    num = 0
    length = len(sobj)
    while num < length:
        for letter in str(sobj[num]):
            if letter in '0123456789':
                num = num + 1
            else:
                return False
    return True



if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')