#!/usr/bin/env python3

'''
    Lab1 
    Part8: Checks if a person is eligible to vote based on their age.
    Class: SRT211
    Student: Raein Nobakht
    Student ID: 103021226
'''

#Ask fo the users age
age = int(input("Enter your age: "))

#Check and see if the number is eligible or not.
if age < 18:
    print("You're not eligible to vote")
else:
    print("You're eligible to vote.")