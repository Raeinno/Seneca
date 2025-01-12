#!/usr/bin/env python3

'''
    Lab1 
    Part4: Program to Determine if a entered Number is Positive, Negative, or Zero.
    Class: SRT211
    Student: Raein Nobakht
    Student ID: 103021226
'''

#Take user number
num = int(input("Please enter a number: "))

#Check to see if the number is positive
if num > 0:
    print("The number is positive")
#Check to see if the number is zero.
elif num == 0:
    print("The number is zero")
#Check to see if the number is negetive.
elif num < 0:
    print("The number is a negetive")

