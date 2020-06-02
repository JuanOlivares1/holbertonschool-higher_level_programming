#!/usr/bin/pthon3
"""Module - defing 'is_same_class' function
"""


def is_kind_of_class(obj, a_class):
    """is_same_class function - returns True if the object is exactly an instance of the specified class
    Args:
        obj (obj): object to compare
        a_class (class): class to compare
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
