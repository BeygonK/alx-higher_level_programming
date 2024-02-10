#!/usr/bin/python3
"""This module defines a class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a class definition of Rectangle
        Attributes:
            Inherits all attributes from main class

        Methods:
            Inherits all methods from main class
    """

    def __init__(self, width, height):
        """This is a constructor"""
        self._height = self.integer_validator("height", height)
        self._width = self.integer_validator("width", width)

    def area(self):
        """Calculates the area of rectangle
            Returns:
                int: area of rectangle
        """
        return self._height * self._width
    
    def __str__(self):
        """Prints string representation"""
        return f"[Rectangle] {self._width}/{self._height}"
