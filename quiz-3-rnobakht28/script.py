#!/usr/bin/env python3
#Raein Nobakht

import sys
   

def read_file(filename):
    try:
        f = open(filename, 'r')
    except:
        print("File Not Found!")
        exit()
    try:
        data = f.read()
    except:
        print("File Not Found!")
        exit()
    try:
        f.close()
    except:
        print("File Not Found!")
        exit()
    return data

try:
    read_file(sys.argv[1])
except:
    print("File Not Found!")
    exit()

if __name__ == "__main__":

    #print(read_file("text.txt"))
    print(read_file(sys.argv[1]))
    ...