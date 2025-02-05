#!/usr/bin/env python3

'''
Raein Nobakht
Lab3
SRT211NIA
'''

# Creating the dictionary
books = {}

id = 0 #Use to give each book an ID
selection = 0 #For the main menu

# Asking the user for a function 
while selection != 5: #Loops the main menu until the users done with the program
    print("")
    print("Press the number corresponding to the option you wish to choose.")
    print("1- Add a new book to the system.")
    print("2- Search for an existing book.")
    print("3- Update details of a book.")
    print("4- Delete a book from the system.")
    print("5- Exit the program.")
    print(books)
    selection = int(input("Please select an option: "))
    print("")

    if selection == 1: 
        #Ask the user for the books information
        title = input("Please enter the title of the book: ")
        author = input("PLease enter the name of the author: ")
        genre = input("Please enter the books genre: ")
        yearofpub = input("Please enter the year of publication: ")
        availability = input("Is the book currently available? ")
        print("please wait while we add the book to our list.")
        #Add the information to the list and give it an ID
        books[id] = {'title': title, 'author': author, 'genre': genre, 'year of publication': yearofpub, 'availability': availability}
        id = id + 1 #Add 1 to the ID count making sure that a new book always has an unused ID
        print("Done! The book is now part of our list.")   

    elif selection == 2:
        usrsearch = input("Please enter the keyword that you're looking for: ") #Ask the user for the a keyword to search
        print("We've found these based on your given word")
        for x, obj in books.items(): #Loop through the main books Dictionary
            for y in obj: # Loop through the Dictionaries that are within the main dictionary
                location = books[x][y] # The current value of the item within the dictionary
                if usrsearch == location: #If the value matches the user input it prints the current dictionary.
                    print(books[x])

    elif selection == 3: 
        upid = int(input("Please enter the books ID: ")) #Ask the user for the ID
        # Ask the user for the new information
        title = input("Please enter the title of the book: ")
        author = input("PLease enter the name of the author: ")
        genre = input("Please enter the books genre: ")
        yearofpub = input("Please enter the year of publication: ")
        availability = input("Is the book currently available? ")
        #Update the new information
        books[upid] = {'title': title, 'author': author, 'genre': genre, 'year of publication': yearofpub, 'availability': availability}
        print("please wait while we update the book in our list.")
        print("Done! The book is now updated.")   

    elif selection == 4:
        delid = int(input("Please enter the ID of the book you wish to remove: ")) # Ask for the books ID
        del books[delid] #delete the ID
        print("The book was successfully deleted")

    elif selection == 5:
        print("Goodbye.") # Break the loop and exit

    else:
        print("Wrong input please try again.")


