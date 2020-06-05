#!/usr/bin/python3
"""Module - json file, repr of obj"""
from json import dumps


def save_to_json_file(my_obj, filename):
    """Function from_json_string - returns the obj representation of a json

    Args:
        my_obj (obj): string to convert
        filename (str): filename
    """
    with open(filename, mode="w", encoding="UTF-8") as fl:
        fl.write(dumps(my_obj))
