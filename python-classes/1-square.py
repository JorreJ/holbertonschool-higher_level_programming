#!/usr/bin/python3
"""
Module: square
Defines a class Square that represents a square.

This module introduces a basic class definition in Python, serving as a
template for creating square objects. The class includes a private attribute
to store the size of the square.
"""


class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square, stored as a private attribute.

    Methods:
        __init__(self, size): Initializes a square with a given size.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.

        Note:
            The size attribute is private and cannot be accessed directly
            outside the class.
        """
        self.__size = size
