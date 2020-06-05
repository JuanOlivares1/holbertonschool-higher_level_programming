#!/usr/bin/python3
"""Module - read n lines of a file"""


def read_lines(filename="", nb_lines=0):
    """Function read_lines - reads n lines of a file en print it

    Args:
        filename (str): name of file to read
        nb_lines (int): number of lines to print
    """
    string = ""
    with open(filename, encoding="UTF-8") as fl:
        if nb_lines <= 0:
            print(fl.read(), end="")
            return
        elif nb_lines > 0:
            while (nb_lines != 0):
                string += fl.readline()
                nb_lines -= 1
            print(string, end="")
