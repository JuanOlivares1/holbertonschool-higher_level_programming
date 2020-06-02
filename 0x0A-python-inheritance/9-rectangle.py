#!/usr/bin/pthon3
"""Module - defing 'is_same_class' function
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """Class Rectangle - defines a rectangle

    inherits from: BaseGeometry

    """
    def __init__(self, width, height):
        """Constructor
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
