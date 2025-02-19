#!/usr/bin/env python3
# Author ID: 103021226

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'
    try:
        x = int(number1) + int(number2)
    except:
        x = "error: could not add numbers"
    return x

def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    try:
        f = open(filename, "r")
        x = list(f)
    except:
        x = "error: could not read file"
    return x

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception