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

    @property
    def size(self):
        """size getter
        Retrun: size"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter
        Args:
            size (int)"""
        self.width = size
        self.height = size

    def __str__(self):
        """graphic representation of rectangle
        Return: string"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.size)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        Args:
            *args
            **kwargs
        """
        atrs = ['id', 'size', 'x', 'y']
        if args is None or len(args) == 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
            return
        for i, v in enumerate(args[:4]):
            setattr(self, atrs[i], v)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
