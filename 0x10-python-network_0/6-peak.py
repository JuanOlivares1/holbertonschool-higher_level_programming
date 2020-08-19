#!/usr/bin/python3
"""Module"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if list_of_integers is None:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    temp = -999999999999
    f = 0

    for num in list_of_integers:
        if num > temp:
            temp = num
            f = 1
    if f == 1:
        return temp
    return None
