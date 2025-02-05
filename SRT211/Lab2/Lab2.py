#!/usr/bin/env python3

'''
Raein Nobakht
Lab2
SRT211NIA
'''

'''
    Initialize a List: Start by initializing an empty list that will store the items.
    Display Menu: Provide a simple text-based menu with options such as:

    Add item to list
    Remove item from list
    Display all items in the list
    Exit the program

    Add Item: When the user selects the option to add an item, prompt them to enter the item's value. Append this item to the list.
    Remove Item: If the user chooses to remove an item, ask them to enter the value of the item they wish to remove. Check if the item exists in the list and remove it if present. If the item is not in the list, display an appropriate message.
    Display List: If the user selects the option to display the list, print all items in the list. If the list is empty, display a message indicating that there are no items to show.
    Exit: Allow the user to exit the program by selecting the exit option. Ensure the program

Note: Submit the .py file for the submission
'''

list1 = [] #Empty list
choice = 0 # For user selection

while choice != 4:

    print("")
    print("Please select the a option.")#Ask the user for an input.
    print("To add a item to list enter 1.")
    print("To remove a item from list enter 2.")
    print("To display all items in the list enter 3.")
    print("To exit the program enter 4")
    choice = int(input(""))
    print("")

    if choice == 1: #Add a item to the list.
        wordtoadd = input("Please enter the word that you wish to add: ")
        list1.append(wordtoadd)
    elif choice == 2: #Remove a item from the list.
        wordtoremove = input("Please enter the word that you wish to remove: ")
        list1.remove(wordtoremove)
    elif choice == 3: #View the list.
        print(list1)
    elif choice == 4: #Exit the program.
        print("Goodbye")
    

