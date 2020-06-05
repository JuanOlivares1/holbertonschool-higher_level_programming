#!/usr/bin/python3
"""Module - from json to obj"""
from json import loads


def from_json_string(my_str):
    """Function from_json_string - returns the obj representation of a json

    Args:
        my_str (str): string to convert

    Return: json string
    """
    return loads(my_str)
