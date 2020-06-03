#!/usr/bin/python3
"""Module - defing 'is_same_class' function
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square - defines a square

    inherits from: Rectangle

    """
    def __init__(self, size):
        """Constructor
        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """str - grafic representation of class
        """
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__size, self.__size)
