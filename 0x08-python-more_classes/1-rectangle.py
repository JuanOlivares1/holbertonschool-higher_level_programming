#!/usr/bin/python3
""" Module - rectangle
"""


class Rectangle:
    """ Class - Rectangle

    Defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # getters & setters
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(slef):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
