#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            string += ch
    return string
