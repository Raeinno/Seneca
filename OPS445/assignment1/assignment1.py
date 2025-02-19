#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
The python code in this file is original work written by
Raein Nobakht. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Raein Nobakht
Semester: Summer 2024
Description: The script should take a date and a number and return "date" + "the given number".
'''

import sys

#date = '01/11/2022'

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "return true if the year is a leap year"

    lyear = year % 4
    if lyear == 0:
        leap_flag = True
    else:
        leap_flag = False  # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        leap_flag = False  # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        leap_flag = True  # this is a leap year

    return leap_flag
    
    ...

def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"

    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month == 2 and leap_year(year):
        mon_max = 29
    else:
        mon_max = mon_dict[month]

    return mon_max
    
    ...

def after(date: str) -> str: 
    '''
    after() -> date for next day in DD/MM/YYYY string format

    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1  # next day
    
    if day > mon_max(mon, year):
        mon += 1
        if mon > 12:
            year += 1
            mon = 1
        day = 1  # if tmp_day > this month's max, reset to 1 
    return f"{day:02}/{mon:02}/{year}"

def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"
    day, mon, year = (int(x) for x in date.split('/'))
    day -= 1  # day before
    
    if day == 0:
        mon -= 1
        if mon == 0:
            year -= 1
            mon = 12
        day = mon_max(mon, year)
    return f"{day:02}/{mon:02}/{year}"
    ...

def usage():
    "Print a usage message to the user"
    if len(sys.argv) == 3:
        try:
            valid_date(sys.argv[1]) == True
        except:
            print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
            sys.exit()
        if valid_date(sys.argv[1]) == False:
            print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
            sys.exit()
        num = 0
        length = len(sys.argv[2])
        while num < length:
            for letter in str(sys.argv[2][num]):
                if letter in '-0123456789':
                    num = num + 1
                else:
                    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
                    sys.exit()
        if sys.argv[2] == 0:
            print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
            sys.exit()
        else:
            return 
    else:
        print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
        sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date"
    day, mon, year = (int(x) for x in date.split('/'))
    if mon <= 0:
        return False
    elif mon > 12:
        return False
    if year <= 0:
        return False
    if mon_max(mon, year) == 31:
        if day <= 0:
            return False
        elif day > 31:
            return False
    elif mon_max(mon, year) == 30:
        if day <= 0:
            return False
        elif day > 30:
            return False
    if mon == 2 and leap_year(year) == True:
        if day <= 0:
            return False
        elif day > 29:
            return False 
    elif mon == 2 and leap_year(year) == False:
        if day <= 0:
            return False
        elif day > 28: 
            return False
    return True
    ...
def day_iter(start_date: str, num: int) -> str:
    "iterates from start date by num to return end date in DD/MM/YYYY"

    while num > 0:
        start_date = after(start_date)
        num = num - 1
    while num < 0:
        start_date = before(start_date)
        num = num + 1
    
    return start_date



    ...

if __name__ == "__main__":
    # check length of arguments
    usage()
    # check first arg is a valid date
    valid_date(sys.argv[1])
    # check that second arg is a valid number (+/-)

    # call day_iter function to get end date, save to x
    x = day_iter(sys.argv[1], int(sys.argv[2]))
    # print(f'The end date is {day_of_week(x)}, {x}.')
    print(f'The end date is {day_of_week(x)}, {x}.')
    
    pass