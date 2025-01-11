#!/usr/bin/env python3

#Raein Nobakht
#OPS445

import sys

#Checking for arguments
if len(sys.argv) == 1:
    print("No args!")
    exit
else :

#Adding the arguments to the list
    arg = str(sys.argv)
 #What lab/investigation/part introduced the topic of conditionals? Lab 2

    args = arg.split("'")

    #Cleaning the list
    args.remove(args[0])
    args.remove(args[0])
    args.remove(']')
    while ', ' in args:
        args.remove(', ')
    
#creating the function 'avg_len'.  What lab/investigation introduced functions with arguments and return values? Lab 3
def avg_len(value1):
    value4 = len(value1)
    while value1 != 0:
       value2 = len(value1[0])
       value3 = value3 + value2
       value1.remove(value1[0])
    finalvalue = value2 / len(value4)
    return finalvalue
print(avg_len)

