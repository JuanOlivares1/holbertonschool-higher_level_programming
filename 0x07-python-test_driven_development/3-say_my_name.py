#!/usr/bin/python3
"""module
"""


def say_my_name(first_name, last_name=""):
    """function - asd
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(first_name, last_name)