#!/usr/bin/python3
"""Module - Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """cosntructor
        Args:
            width (int)
            height (int)
            x (int)
            y (int)
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter
        Return: width"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter
        Args:
            width (int)"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """width getter
        Return: width"""
        return self.__height

    @height.setter
    def height(self, height):
        """width setter
        Args:
            width (int)"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """width getter
        Return: width"""
        return self.__x

    @x.setter
    def x(self, x):
        """width setter
        Args:
            width (int)"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """width getter
        Return: width"""
        return self.__y

    @y.setter
    def y(self, y):
        """width setter
        Args:
            width (int)"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """finds the area of rectangle
        Return: (int) area"""
        return self.width * self.height

    def display(self):
        """displays in stdout a representtion of rectangle"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """graphic representation of rectangle
        Return: string"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        Args:
            *args
            **kwargs
        """
        atrs = ['id', 'width', 'height', 'x', 'y']
        if args is None or len(args) == 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
            return
        for i, v in enumerate(args[:5]):
            setattr(self, atrs[i], v)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
