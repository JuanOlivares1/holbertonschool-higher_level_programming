#!/usr/bin/python3
"""Module - Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """cosntructor
        Args:
            size(int)
            x (int)
            y (int)
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """graphic representation of rectangle
        Return: string"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.width, self.height)
