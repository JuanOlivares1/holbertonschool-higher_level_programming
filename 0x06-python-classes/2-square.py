#!/usr/bin/python3
"""Python module - Cwrite a class Square that defines a square by size
"""


class Square:
    """Square
    """
    def __init__(self, size=0):
        """__init__ constructor

        Args:
            size (int): square size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
