#!/usr/bin/python3
"""Module"""


def class_to_json(obj):
    """Function
    Arguments:
        obj (obj): object

    Returns: returns the dictionary description of object
    """
    return obj.__dict__
