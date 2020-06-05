#!/usr/bin/python3
"""Module - write to a file"""


def write_file(filename="", text=""):
    """Function write_file - writes a string to a text file

    Args:
        filename (str): name of file to read
        text (str): text to write into the file

    Return: number of characters written
    """
    with open(filename, mode="w", encoding="UTF-8") as fl:
        i = fl.write(text)
    return i
