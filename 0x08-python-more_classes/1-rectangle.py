#!/usr/bin/python3
""" Module - rectangle
"""


class Rectangle:
    """ Class - Rectangle

    Defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    # getters
    @property
    def width(self):
        return self.__width

    @property
    def height(slef):
        return self.__height

    # setters
    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
