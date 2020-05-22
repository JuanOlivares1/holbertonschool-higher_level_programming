#!/usr/bin/python3
"""
Module - add function.

This file only contains a function to test by docstrings
"""


def add_integer(a, b=98):
    """
    Function add_integer - Adds two numbers and returns result
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
