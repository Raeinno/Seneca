#!/usr/bin/env python3

'''
Raein Nobakht
Lab4
SRT211NIA
'''


userinput = ""

while userinput != "exit": # Asking for the users input.
    print("")
    print("Please type the initionals for the calculation that you wish to do.")
    print("Type add for addition.\nType sub for subtraction.\nType mul for multiplication.\nType div for division.")
    print("Type exit to exit the system.")
    userinput = input("Enter your choice: ")

    if userinput == "exit": #Checking if the user wants to exit or not.
        print("Goodbye")
    else:
        try:#Checking to see if the given input is correct.

            num1 = int(input("Please enter the first number: "))#Asking for the two numbers.
            num2 = int(input("please enter the second number: "))

            if userinput == "add":#calculations.
                print("The addition of the two numbers is: " + str(num1+num2))
            elif userinput == "sub":
                print("The subtraction of the two numbers is: " + str(num1-num2))
            elif userinput == "mul":
                print("The result of the multiplication is: " + str(num1*num2))
            elif userinput == "div":
                try:#Checking and making sure that the second number isn't zero for division.
                    print("The result of the division is: " + str(num1/num2))
                except ZeroDivisionError:
                    print("Can not divide by zero.")
        except ValueError:
            print("invalid inputs")