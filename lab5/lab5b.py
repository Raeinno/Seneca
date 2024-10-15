#!/usr/bin/env python3
# Author ID: 103021226

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r')
    data = f.read()
    f.close()
    return data

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    f = open(file_name, 'r')
    data = f.read()
    # return its entire contents as a list of lines without new-line characters
    line = data.split('\n')
    line.remove("")
    return line

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    f = open(file_name, 'a')
    content = f.write(string_of_lines)
    f.close()

    return content

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    f = open(file_name, 'w')
    for char in list_of_lines:
        content = f.write(str(char) + '\n')
    f.close()

    return content

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    x = 0
    f = open(file_name_read, 'r')
    f_content = list(f)
    w = open(file_name_write, 'w')

    for char in f_content:
        w.write(str(x + 1))
        w.write(str(":"))
        content = w.write(str(char))
        x = x + 1
        #final = w.write(str(content))
    
    return content

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))