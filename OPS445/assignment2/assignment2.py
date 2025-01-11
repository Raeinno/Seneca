#!/usr/bin/env python3

'''
OPS445 Assignment 2
Program: assignment2.py 
Author: Raein Nobakht
Semester: Summer

The python code in this file is original work written by
Raein Nobakht. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: <Enter your documentation here>

'''

import argparse
import os, sys

def parse_command_args() -> object:
    "Set up argparse here. Call this function inside main."
    parser = argparse.ArgumentParser(description="Memory Visualiser -- See Memory Usage Report with bar charts",epilog="Copyright 2023")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    # add argument for "human-readable". USE -H, don't use -h! -h is reserved for --help which is created automatically.
    parser.add_argument("-H", "--human-readable", action='store_true', help="Prints sizes in human readable format")
    # check the docs for an argparse option to store this as a boolean.
    parser.add_argument("program", type=str, nargs='?', help="if a program is specified, show memory use of all associated processes. Show only total use is not.")
    args = parser.parse_args()
    return args
# create argparse function
# -H human readable
# -r running only

def percent_to_graph(percent: float, length: int=20) -> str:
    "turns a percent 0.0 - 1.0 into a bar graph"
    #yout-ymin / ymax- ymin = xin - xmin / xmax - xmin
    #yout - 0 / 1 - 0 = xin - 0 / xmax - 0
    #yout = xin / xmax
    #yout = the number between 0.0 - 1.0 /// xin = num of # in graph /// xmax = maximum num of #

    loading = "" # Bar graph
    location = length * percent #yout = xin / xmax
    round = int(location) # For rounding

    #Rounding down or up formula
    check = location - round
    if check >= 0.5:
        round = round + 1
    space = length - round 
    while round > 0:
        loading = loading + '#'
        round = round - 1

    # Creating the required spaces in a graph
    while space > 0:
        loading = loading + " "
        space = space - 1
    #loading = loading + "'"
    return loading
    ...
# percent to graph function

def get_sys_mem() -> int:
    "return total system memory (used or available) in kB"
    f = open("/proc/meminfo", "r")
    messydata = f.readlines() # reading the file
    memtotaltext = messydata[0] # grabing the memtotal
    listmemtotal = memtotaltext.split(' ') # spliting the line
    f.close()
    while listmemtotal[1] == '': # removing the empty spaces
        listmemtotal.remove('')
    memtotal = int(listmemtotal[1]) # grabing the number

    return memtotal
    ...

def get_avail_mem() -> int:
    "return the availabe memory that is currently not in use"
    #“Memory in use” = Total Memory - Available Memory
    f = open("/proc/meminfo", "r") 
    messydata = f.readlines() # reading the file
    memavailabletext = messydata[2] # grabing the available memory
    listavailabletotal = memavailabletext.split(' ') # spliting the line
    f.close()
    while listavailabletotal[1] == '': # removing the empty spaces
        listavailabletotal.remove('')
    memavailable = int(listavailabletotal[1]) # grabing the number
    #meminuse = get_sys_mem() - memavailable

    return memavailable
    ...
def pids_of_prog(app_name: str) -> list:
    "given an app name, return all pids associated with app"
    command = "pidof " + app_name # creating the command
    system = os.popen(command) # running the command
    system1 = system.read() # reading the command
    system2 = system1.split() # spliting each name

    return system2
    ...

def rss_mem_of_pid(proc_id: str) -> int:
    "given a process id, return the resident memory used, zero if not found"
    y = 0 # empty varriable to use later
    try: # checking and making sure that the app exists
        f = open(f"/proc/{str(proc_id)}/smaps", "r") 
    except:
        return 0
    #f = open(f"/proc/{pid}/smaps", "r")
    
    for row in f: # going through the file
        messydata = row
        if messydata.startswith("Rss"): #grabbing each line that starts with Rss
            x = messydata.split() #spliting it
            y += int(x[-2]) # adding the up each number
    f.close()
    return y
    ...

def bytes_to_human_r(kibibytes: int, decimal_places: int=2) -> str:
    "turn 1,024 into 1 MiB, for example"
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']  # iB indicates 1024
    suf_count = 0
    result = kibibytes 
    while result > 1024 and suf_count < len(suffixes):
        result /= 1024
        suf_count += 1
    str_result = f'{result:.{decimal_places}f} '
    str_result += suffixes[suf_count]
    return str_result

def final():

    if args.program:
        
        if args.human_readable:
            x =  pids_of_prog(args.program) # getting the pids of the program
            e = 0
            for num in x:
                a = rss_mem_of_pid(num)
                b = get_sys_mem()
                e += a # getting the total memory
                y = a * 100 / b # turning the memory into a percent
                z = y / 100 # turns the memory into a format that can be used to make the graph
                c = percent_to_graph(z, args.length) # getting the graph

                print(f"{num: <15}[{c}| {round(y)}%] {bytes_to_human_r(a)}/{bytes_to_human_r(b)}")

            y = e * 100 / b # turning the total memory into a percent
            z = y / 100 # turns the memory into a format that can be used to make the graph
            c = percent_to_graph(z, args.length) # getting the graph
            print(f"{args.program: <15}[{c}| {round(y)}%] {bytes_to_human_r(e)}/{bytes_to_human_r(b)}")
            
        else:
            x =  pids_of_prog(args.program) # getting the pids of the program
            e = 0
            for num in x:
                a = rss_mem_of_pid(num)
                b = get_sys_mem()
                e += a # getting the total memory
                y = a * 100 / b # turning the memory into a percent
                z = y / 100 # turns the memory into a format that can be used to make the graph
                c = percent_to_graph(z, args.length) # getting the graph

                print(f"{num: <15}[{c}| {round(y)}%] {a}/{b}")

            y = e * 100 / b # turning the total memory into a percent
            z = y / 100 # turns the memory into a format that can be used to make the graph
            c = percent_to_graph(z, args.length) # getting the graph
            print(f"{args.program: <15}[{c}| {round(y)}%] {e}/{b}")
    else:
        x = get_sys_mem() - get_avail_mem()  # getting the current memory in use
        b = get_sys_mem()
        y = x * 100 / b # turning the memory into a percent
        z = y / 100 # turns the memory into a format that can be used to make the graph
        c = percent_to_graph(z, args.length) # getting the graph
        if args.human_readable:
            print(f"Memory         [{c}| {round(y)}%] {bytes_to_human_r(x)}/{bytes_to_human_r(b)}")
        else:
            print(f"Memory         [{c}| {round(y)}%] {x}/{b}")
        ...
    return

if __name__ == "__main__":
    args = parse_command_args()
    if not args.program:
        ...
    else:
        ...
    final()
    #print(percent_to_graph(float(sys.argv[1])))
    # process args
    # if no parameter passed, 
    # open meminfo.
    # get used memory
    # get total memory
    # call percent to graph
    # print

    # if a parameter passed:
    # get pids from pidof
    # lookup each process id in /proc
    # read memory used
    # add to total used
    # percent to graph
    # take total our of total system memory? or total used memory? total used memory.
    # percent to graph.

#testing
#print(percent_to_graph(0.33))
#print(get_sys_mem())
#print(get_avail_mem())
#print(pids_of_prog("firefox"))
#print(rss_mem_of_pid(5706))
#print(rss_mem_of_pid(573412141684612684123)