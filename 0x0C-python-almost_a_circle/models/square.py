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
        self.size = size

    @property
    def size(self):
        """size getter
        Retrun: size"""
        return self.__size

    @size.setter
    def size(self, size):
        """size setter
        Args:
            size (int)"""
        self.width = size
        self.height = size
        self.__size = size

    def __str__(self):
        """graphic representation of rectangle
        Return: string"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.size)
