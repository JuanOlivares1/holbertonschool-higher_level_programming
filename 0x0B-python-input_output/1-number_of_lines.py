#!/usr/bin/python3
"""Module - read a file and get number of lines"""


def number_of_lines(filename=""):
    """Function number_of_lines - reads a file and gets the number of lines

    Args:
        filename (str): name of file to read

    Return: number of lines
    """
    with open(filename, encoding="UTF-8") as fl:
        i = 0
        for line in fl:
            i += 1
    return i
