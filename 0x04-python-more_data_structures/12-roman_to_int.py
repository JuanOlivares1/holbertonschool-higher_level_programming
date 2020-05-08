#!/usr/bin/python3
def roman_to_int(roman_string):
    values = {'M': 1000, 'D': 500, 'C': 100,
               'L': 50, 'X': 10, 'V': 5, 'I': 1}
    res = 0;
    for letter in roman_string:
        val = values[letter]
        if res == 0:
            temp = val
            res += val
            continue
        res += val
        if temp < val:
            res -= (temp * 2)
        temp = val
    return res
