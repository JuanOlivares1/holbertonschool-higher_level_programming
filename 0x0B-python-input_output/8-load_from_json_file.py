#!/usr/bin/python3
"""Module - creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Function load_from_json_file - creates an Object from a “JSON file”

    Args:
        filename (str): filename

    Return: object from json
    """
    with open(filename, mode="r", encoding="UTF-8") as fl:
        return json.loads(fl.read())
