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
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """This is a constructor method"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """This is a getter"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
