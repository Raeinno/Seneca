#!/usr/bin/env python3

'''
    Lab1 
    Part3: Calculate the Area of a Circle based on radius entered by user (follow pi*r*r euation).
    Class: SRT211
    Student: Raein Nobakht
    Student ID: 103021226
'''

#Ask the user for the radius
radius = int(input("Enter the radius of the circle: "))

#Calculate the area of the circle
calculation = (radius * radius) * 3.14159

#Output
print("The area of the circle is " + str(calculation))