#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        values = {'M': 1000, 'D': 500,
                  'C': 100, 'L': 50,
                  'X': 10, 'V': 5, 'I': 1}
        res = 0
        for letter in roman_string:
            val = values[letter]
            if res != 0:
                res += val
                if temp < val:
                    res -= (temp * 2)
                temp = val
            else:
                res += val
                temp = val
        return res
    return 0
