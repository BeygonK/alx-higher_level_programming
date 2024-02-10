#!/usr/bin/python3
"""This module defines a square class"""


Rectangle = __import__('9-rectangle').Rectangle
class Square(Rectangle):
    """This is a definition of  class
        Attributes:
            inherits from parent class
        Methods:
            inherites from the parent class
    """
    def __init__(self, size):
        """This is a constructor"""
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """This is area() method"""
        return self.__size * self.__size

