#!/usr/bin/python3
"""Module - defing 'is_same_class' function
"""


class BaseGeometry():
    """class BaseGeometry - empty class
    """
    def area(self):
        """function area() - raise an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function integer_validator() - validates value
        Args:
            name (str): name of variable
            values (int): integer to validate
        """
        if type(value) not in [int]:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
