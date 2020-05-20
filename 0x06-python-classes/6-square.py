#!/usr/bin/python3
"""Python module - write a class Square that defines a square by size
"""


class Square:
    """Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """__init__ constructor

        Args:
            size (int): square size
            position (tuple): position of square in space
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """size getter
        """
        return self.__position

    @position.setter
    def position(self, position):
        """size setter
        """
        if type(position) != tuple or\
           type(position[0]) != int or\
           position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """returns the current area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with '#' characters
        """
        if self.__size == 0:
            print()
        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.position[0], end="")
            print("#" * self.__size)
