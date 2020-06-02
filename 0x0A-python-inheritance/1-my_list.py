#!/usr/bin/python3
"""Module - class MyList(list)
"""


class MyList(list):
    """MyList class - inhertit from list class
    """
    def __init__(self):
        """constructor for MyList class
        """
        list.__init__(self)

    def print_sorted(self):
        """prints the list, but sorted
        """
        new = self[:]
        new.sort()
        print(new)
