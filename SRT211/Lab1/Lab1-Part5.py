#!/usr/bin/env python3

'''
    Lab1 
    Part5: Program to Find the Largest of Three Numbers.
    Class: SRT211
    Student: Raein Nobakht
    Student ID: 103021226
'''

#Take the 3 number from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

#Check and see which number is the largest
if num1 > num2 and num1 > num3:
    print("Number " + str(num1) + " is the largest number.")
elif num2 > num1 and num2 > num3:
    print("Number " + str(num2) + " is the largest number.")
elif num3 > num1 and  num3 > num2:
    print("Number " + str(num3) + " is the largest number.")
#If no number is the largest
else:
    print("2 or more numbers are tied for the largest number")