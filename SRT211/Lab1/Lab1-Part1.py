#!/usr/bin/env python3

'''
    Lab1 
    Part1: Program to Convert Kilometers to Miles. Take kilometer as the input from user.
    Class: SRT211
    Student: Raein Nobakht
    Student ID: 103021226
'''

#Ask for the kilometer
kilometer = input("Please enter a value in Kilometers: ")

#Convert the number to miles
mile = int(kilometer) * 0.62137

print("Your number is: " + str(mile))
