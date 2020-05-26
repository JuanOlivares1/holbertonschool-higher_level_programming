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

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            string += "#" * self.__width
            if i < self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", " +\
            str(self.__height) + ")"

    def __del__(self):
        print("Bye rectangle...")

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

    # methods
    def area(self):
        """ Method - Returns the area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Method - Returns the perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
