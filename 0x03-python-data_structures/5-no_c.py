#!/usr/bin/python3

def no_c(string):
    new_string = ''
    for char in string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
