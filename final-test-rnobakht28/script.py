#!/usr/bin/env python3
#Raein Nobakht
#8/16/2024


test_str = "Raein" #Outside of your main block, create a variable called test_str and enter your name as its value.
places = ["Canada", "Toronto", "New York", "New port", "Old Port", "Old York"] #Outside of your main block, create a list called places. Fill it with at least 4 different names of places.
v_places = [] #Outside of your main blocks, create an empty list called v_places.

#Outside of your main block, create a function called cap_vowel.
def  cap_vowel(first: str):
    x = first[0]
    
    if x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        return True
    else: 
        return False
    ...

#Create a function called file_op. This function should accept a list and filename as parameters and return nothing.
def file_op(list1: list, name: str):
    f = open(name, "a")
    for letter in list1:
        f.write(f"{str(letter)}\n")
    f.close()

if __name__ == '__main__': 

    print(f"My name is {test_str}") #Inside your main block, print the following: My name is <value> where <value> is the value of test_str.

    x = len(test_str) #Inside your main block, write code to test the length of test_str.
    if x < 8:
        print("my name is short.")
    else:
        print("my name is long.")

    assert cap_vowel('Toronto') == False
    assert cap_vowel('Ottawa') == True

    #Inside your main block, use an appropriate loop to iterate through places and for each place, use your function to get a result. (1)
    for letter in places:
        x = cap_vowel(letter)
        if x == True:
            v_places.append(letter)

    #Call your file_op function inside main, and pass in v_places and test_str as the arguments. In other words, you should be using your name as the filename you write to.
    file_op(v_places, test_str)

    ...


