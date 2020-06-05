#!/usr/bin/python3
"""Module - from obj to json"""
from json import dumps


def to_json_string(my_obj):
    """Function to_json_string - returns the JSON representation of an object

    Args:
        my_obj (obj): object to convert

    Return: json string
    """
    return dumps(my_obj)
