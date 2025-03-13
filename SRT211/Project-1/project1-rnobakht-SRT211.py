#!/usr/bin/env python3

'''
Raein Nobakht
Project1
SRT211NIA
'''
'''
Quiz Game:
•Features:
    Question Setup: Load questions and answers into the system.
    Quiz Execution: Run through the questions, accept user answers, and keep score.
    Results Display: Show the final score and correct answers after the quiz.
•Learning Objectives: Lists, conditionals, loops, and basic functions.
'''
#Variables
difficulty = 0 #For difficulty selection
userinput = "" #For taking user inputs
currentquestion = 0 #For printing the correct question
points = 0 #For counting users points.

#Questions and answers
questionseasy = {"What is 2 + 2 eguals? ": "4", 
                 "How to spell 'Banana'(All lower cap)? ": "banana",
                  "If you have 4 apples and your friend takes 2 of them how many apples do you now have(no space between the apple and the number)? ": "2apples",
                  "What's 5 - 4 equal to? ": "1",
                    "If x = 4 + 5, what is x? ": "9"}
questionsmedium = {"5 + 4 + 77 + (5 X 2) equals to: ": "96", 
                   " If the radius of a circle is 10, whats the area of the circle(pi = 3.14): ":"314", 
                   "What is the capital of Japan(All lower cap)?": "tokyo",
                   "4 - 6 + 5 X (7 - 6) equals to: ": "3",
                   "5 + 9 X 3 + 7 - 20 equals to: ": "19"}
questionshard ={"55 - 27 + 50 X 10 equals to: ": "528",
                "Type pi down to the 8th digit: ": "3.1415926",
                "What's the surface area of a sphere with a radius of 33? ": "13685",
                "((((99 + 4) X 7) / (8 + 67) - 5) X (55 - 4 X 0)) + 56 - 77 X 1 equals to: ": "-21", 
                "What's the name of the second highest mountain on earth? ": "K2"}

#Asking for a difficulty
while (difficulty != 5):

    difficulty = int(input("Please Select your difficulty.\n"
    "1 for easy(1 point per question)\n"
    "2 for medium(2 points per question\n"
    "3 for hard(3 points per question)\n"
    "4 to do all difficulties\n"
    "5 to end the quiz and see your score and answers\n"))

    if not(0 < difficulty < 6):
        print("\nWrong input. Try again.\n")

    if (difficulty == 1 or difficulty == 4): # Difficulty 1 questions
        print("\nDifficulty 1\n")
        keylist = list(questionseasy.keys()) # Turning the keys values so that it can be used for the loop
        currentquestion = 0 # Reset the question counter.
        for x in keylist: # Loop through each question if the answer is right, It'll add it to the points
            userinput = input(keylist[currentquestion])
            if  userinput == questionseasy[keylist[currentquestion]]:
                points += 1
            currentquestion += 1
            if currentquestion < 5:
                print("\nNext Question")

    if (difficulty == 2 or difficulty == 4): # Difficulty 2 questions
        print("\nDifficulty 2\n")
        keylist = list(questionsmedium.keys()) # Turning the keys values so that it can be used for the loop
        currentquestion = 0 # Reset the question counter.
        for x in keylist: # Loop through each question if the answer is right, It'll add it to the points
            userinput = input(keylist[currentquestion])
            if  userinput == questionsmedium[keylist[currentquestion]]:
                points += 2
            currentquestion += 1
            if currentquestion < 5:
                print("\nNext Question")

    if (difficulty == 3 or difficulty == 4): # Difficulty 3 questions
        print("\nDifficulty 2\n")
        keylist = list(questionshard.keys()) # Turning the keys values so that it can be used for the loop
        currentquestion = 0 # Reset the question counter.
        for x in keylist: # Loop through each question if the answer is right, It'll add it to the points
            userinput = input(keylist[currentquestion])
            if  userinput == questionshard[keylist[currentquestion]]:
                points += 3
            currentquestion += 1
            if currentquestion < 5:
                print("\nNext Question")

#Show answers
print("\nThe answer to the questions are:\n")

keylist = list(questionseasy.keys()) # Turning the keys values so that it can be used for the loop
currentquestion = 0 # Reset the question counter.
for x in keylist: # Print question 1 answers
    print("Question: " + keylist[currentquestion])
    print("Answer: " + questionseasy[keylist[currentquestion]])
    currentquestion += 1

keylist = list(questionsmedium.keys()) # Turning the keys values so that it can be used for the loop
currentquestion = 0 # Reset the question counter.
for x in keylist: # Print question 2 answers
    print("Question: " + keylist[currentquestion])
    print("Answer: " + questionsmedium[keylist[currentquestion]])
    currentquestion += 1

keylist = list(questionshard.keys()) # Turning the keys values so that it can be used for the loop
currentquestion = 0 # Reset the question counter.
for x in keylist: # Print question 3 answers
    print("Question: " + keylist[currentquestion])
    print("Answer: " + questionshard[keylist[currentquestion]])
    currentquestion += 1

print("\nGood Job!\nYour score is: " + str(points))