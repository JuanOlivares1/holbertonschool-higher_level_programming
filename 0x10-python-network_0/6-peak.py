#!/usr/bin/python3
"""Module"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    if not len(list_of_integers):
        return None
    else:
        list_of_integers.sort()
        return list_of_integers[-1]
