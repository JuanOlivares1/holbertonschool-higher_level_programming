#!/usr/bin/python3
"""Module - read a file"""


def read_file(filename=""):
    """Function read_file - reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): name of file to read
    """
    with open(filename, encoding="UTF-8") as fl:
        print(fl.read(), end="")
