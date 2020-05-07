#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    if my_list:
        numbers = set(my_list)
        for i in numbers:
            res += i
    return res
