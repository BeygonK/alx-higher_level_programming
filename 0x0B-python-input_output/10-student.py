#!/usr/bin/python3
"""This module defines class"""


class Student:
    """This is a definition of a class"""
    def __init__(self, first_name, last_name, age):
        """This is a constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This is a method"""
        if attrs is None:
            return self.__dict__
        else:
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
            return json_dict
