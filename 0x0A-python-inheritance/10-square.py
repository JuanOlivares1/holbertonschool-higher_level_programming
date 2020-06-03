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
        Rectangle.integer_validator(self, "size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size
