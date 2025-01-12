#!/usr/bin/env python3

'''
    Lab1 
    Part7: Calculates the price of a movie ticket based on the age of the customer. Different age groups have different ticket prices.
    Class: SRT211
    Student: Raein Nobakht
    Student ID: 103021226
'''

#Ticket prices based on age.
sixorless = 8.99
twelveandless = 12.99
twelveormore = 14.99
eighteenormore = 16.99

#Ask for users age.
age = int(input("Enter your age: "))

#Calculate the price of the ticket
if age <= 6:
    print("Your Ticket price is " + str(sixorless))
elif age > 6 and age <= 12:
    print("Your Ticket price is " + str(twelveandless))
elif age > 12 and age < 18:
    print("Your Ticket price is " + str(twelveormore))
else:
    print("Your Ticket price is " + str(eighteenormore))