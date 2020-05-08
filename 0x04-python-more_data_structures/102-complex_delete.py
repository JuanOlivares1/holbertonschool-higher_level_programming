#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    values = []
    for k, v in a_dictionary.items():
        if v == value:
            values.append(k)
    for k in values:
        a_dictionary.pop(k)
    return a_dictionary
