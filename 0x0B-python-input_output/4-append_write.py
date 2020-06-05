#!/usr/bin/python3
"""Module - append to a file"""


def append_write(filename="", text=""):
    """Function append_write - appends a string at the end of a text file

    Args:
        filename (str): name of file to read
        text (str): text to write into the file

    Return: number of characters written
    """
    with open(filename, mode="a", encoding="UTF-8") as fl:
        i = fl.write(text)
    return i
