#!/usr/bin/env python3

'''
    Lab1 
    Part6: create a grade calculater as discussed in class.
    Class: SRT211
    Student: Raein Nobakht
    Student ID: 103021226
'''
#Asking the users for 2 number.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#Asking the user what kind of calculation he wants to do.
print("Choose the number associated for the calculation.")
print("To calculate the sum press 1.")
print("To subtract the numbers press 2.")
print("For multiplication press 3.")
print("For division press 4.")
print("Press 5 to do all.")
choice = input()

#Doing the calculations
if int(choice) == 1:
    print("The sum of the two numbers is " + str(num1+num2))

elif int(choice) == 2:
    print("The subtraction of the two numbers is " + str(num1-num2))

elif int(choice) == 3:
    print("The result of the multiplication is: " + str(num1*num2))

elif int(choice) == 4:
    print("The result of the division is: " + str(num1/num2))

elif int(choice) == 5:
    print("The sum of the two numbers is " + str(num1+num2))
    print("The subtraction of the two numbers is " + str(num1-num2))
    print("The result of the multiplication is: " + str(num1*num2))
    print("The result of the division is: " + str(num1/num2))

else:
    print("Wrong input, goodbye.")
