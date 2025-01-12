#!/usr/bin/env python3

'''
    Lab1 
    Part2: Program to Check wheather entered Number is Even or Odd.
    Class: SRT211
    Student: Raein Nobakht
    Student ID: 103021226
'''

num = int(input("Please enter a number: "))

while num > 1:
    num = num % 2
else:
    if num == 0:
        print("The number is even")
    else:
        print("the number is odd")