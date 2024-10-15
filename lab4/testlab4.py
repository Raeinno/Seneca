#!/usr/bin/env python3



'''
t1 = ('Prime', 'Ix', 'Secundus', 'Caladan')
t2 = (1, 2, 3, 4, 5, 6)



print(t1[0])
print(t2[2:4])



print('Ix' in t1)
print('Geidi' in t1)



list2 = [ 'uli101', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635' ]


list2[0]= 'ica100'
print(list2[0])
print(list2)


t2[1] = 10

t3 = t2[2:3]'''


'''
s1 = {'Prime', 'Ix', 'Secundus', 'Caladan'}
s2 = {1, 2, 3, 4, 5}
s3 = {4, 5, 6, 7, 8}

#print(s1[0])

print('Ix' in s1)
print('Geidi' in s1)

print(s2)
print(s3)



print(s2 | s3)         # returns a set containing all values from both sets
print(s2.union(s3))    # same as s2 | s3

print(s2 & s3)             # returns a set containing all values that s2 and s3 share
print(s2.intersection(s3)) # same as s2 & s3

print(s2)
print(s3)
print(s2 - s3)             # returns a set containing all values in s2 that are not found in s3
print(s2.difference(s3))   # same as s2 - s3


print(s2 ^ s3)                     # returns a set containing all values that both sets DO NOT share
print(s2.symmetric_difference(s3)) # same as s2 ^ s3
'''

'''
l2 = [1, 2, 3, 4, 5]
l3 = [4, 5, 6, 7, 8]
temporary_set = set(l2).intersection(set(l3))
new_list = list(temporary_set)  # set() can make lists into sets. list() can make sets into lists.
print(new_list) '''


#dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Postal Code': 'M3J3M6', 'Province': 'ON'}


#print(dict_york)
#print(dict_york.values())

#print(dict_york.keys())

#print(dict_york['Address'])
#print(dict_york['Postal Code'])
#list_of_keys = list(dict_york.keys())
#print(list_of_keys[0])


'''for key in list_of_keys:
    print(key)
for value in dict_york.values():
    print(value)'''

'''
course_name = 'Open System Automation'
course_code = 'OPS445'
course_number = 445


print(course_name)
print(course_code)
print(str(course_number))
print(course_name + ' ' + course_code + ' ' + str(course_number))

print('Line 1\nLine 2\nLine 3\n')
print("")

print(course_name.lower())         # Returns a string in lower-case letters
print(course_name.upper())         # Returns a string in upper-case letters
print(course_name.swapcase())      # Returns a string with upper-case and lower-case letters swapped
print(course_name.title())         # Returns a string with upper-case first letter of each word, lowercase for remaining text
print(course_name.capitalize())    # Returns a string with upper-case first letter only, lowercase for remaining text
print("")

lower_name = course_name.lower()    # Save returned string lower-case string inside new string variable
print(lower_name)
print("")

lower_name.split(' ')       # Provide the split() function with a character to split on
print("")

list_of_strings = lower_name.split(' ')     # Split string on spaces and store the list in a variable
print(list_of_strings)                      # Display list
print(list_of_strings[0])                   # Display first item in list
print("")

list_of_strings[0].upper()           # Use the function after the index to affect a single string within a list
first_word = list_of_strings[0]
print(first_word)'''

'''
course_name = 'Open System Automation'
course_code = 'OPS445'
course_number = 445
print(course_code[0])                          # Print the first character in course_code
print(course_code[2])                          # Print the third character in course_code
print(course_code[-1])                         # Print the last character in course_code
print(str(course_number)[0])                   # Turn the integer into a string, return first character in that string, and print it
print(course_code[0] + course_code[1] + course_code[2])
print("")

print(course_name[0:4])                 # Print the first four characters (values of index numbers 0,1,2, and 3) 
first_word = course_name[0:4]           # Save this substring for later use
print(course_code[0:3])                 # Print the first three characters (values of index numbers 0,1,and 2)
print("")

print(course_name[0:4])                 # Print the first four characters (values of index numbers 0,1,2, and 3) 
first_word = course_name[0:4]           # Save this substring for later use
print(course_code[0:3])                 # Print the first three characters (values of index numbers 0,1,and 2)
print("")

course_name = 'Open System Automation'
print(course_name[12:])                        # Print the substring '12' index until end of string
print(course_name[5:])                         # Print the substring '5' index until end of string
print(course_name[-1])                         # Print the last character
print("")

course_name = 'Open System Automation'
print(course_name[-1])
print(course_name[-2])
print("")

course_name = 'Open System Automation'
print(course_name[-10:])                            # Return the last ten characters
print(course_name[-10:-6])                          # Try and figure out what this is returning 
print(course_name[0:4] + course_name[-10:-6])       # Combine substrings together
substring = course_name[0:4] + course_name[-10:-6]  # Save the combined substring as a new string for later
print(substring)'''

text = 'Seneca'
letter = text[1]
print(letter)

text = 'Seneca'
offset = 0
length = len(text)
while offset < length:
    print(offset, text[offset])
    offset = offset + 1

s1 = 'Seneca'
print(s1, 'contains letter s? ->', 's' in s1)
print(s1, 'contains letter S? ->', 'S' in s1)

for letter in text:
    print(letter)

def find(text,char):
    for letter in text:
        if letter == char:
             return True
    return False

if __name__ == '__main__':
    s1 = 'Seneca'
    print(s1,'contains letter s? ->',find(s1,'s'))
    print(s1,'contains letter S? ->',find(s1,'S'))


def is_vowel(char):
    if char in 'aeiou':
        return True
    return False
      
if __name__ == '__main__':
    text = 'Seneca'
    vowel_count = 0
    for char in text:
        if is_vowel(char):
             vowel_count = vowel_count + 1
    print('There are',vowel_count,'vowel(s) in',text)