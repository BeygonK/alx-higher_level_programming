#!/usr/bin/python3
"""This module creates a class"""


from .base import Base


class Rectangle(Base):
    """This is a definition of a class
    Attributes:
        __width: int
        __height: int
        __x: int
        __y: int
    Methods:
        getters and setters
        area: returns area
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """This is a constructor method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """This is a getter"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """This method returns area"""
        return self.__width * self.__height

    def display(self):
        """This method displays rectangle"""
        for _ in range(self.__width):
            for _ in range(self.__height):
                print("#", end="")
            print()
