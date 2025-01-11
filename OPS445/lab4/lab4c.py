#!/usr/bin/env python3

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # Place code here - refer to function specifics in section below
    dict1 = dict()
    while values and keys != 0:
        for x in keys:
            dict1[keys[0]] = values[0]
            keys.remove(keys[0])
            values.remove(values[0])

        
        
        
    return dict1




def shared_values(dict1, dict2):
    #Place code here - refer to function specifics in section below

    dict1values = set(dict1.values())
    dict2values = set(dict2.values())
    return dict1values & dict2values


if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)