#!/usr/bin/python3
"""This is a module with add function"""


def add_integer(a, b=98):
    """ This is a function that adds two integers
        
        args:
            a(int): first paramater
            b(int): second paramater

        Returns:
            int: sum of two numbers

        Raises:
            TypeError: if a or b is not integer or float

    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    
    a = int(a)
    b = int(b)

    return a + b
