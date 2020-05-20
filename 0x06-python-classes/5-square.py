#!/usr/bin/python3
"""Python module - write a class Square that defines a square by size
"""


class Square:
    """Square
    """
    def __init__(self, size=0):
        """__init__ constructor

        Args:
            size (int): square size
        """
        self.size = size

    @property
    def size(self):
        """size getter
        """
        return self.__size

    @size.setter
    def size(self, size):
        """size setter
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the current area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with '#' characters
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()
