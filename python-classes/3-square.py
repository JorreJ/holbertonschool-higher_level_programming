#!/usr/bin/python3
"""
Module: square
Defines a class Square that represents a square.

This module introduces a basic class definition in Python, serving as a
template for creating square objects. The class includes a private attribute
to store the size of the square and ensures that the size follows specific
validation rules. Also provides a method to calculate the area of the square.
"""


class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square, stored as a private attribute.

    Methods:
        __init__(self, size=0): Initializes a square with a given size,
                                ensuring it is a non-negative integer.
        area(self): Returns the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int, optional): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.

        Note:
            The size attribute is private and cannot be accessed directly
            outside the class.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square, calculated as size squared.
        """
        return self.__size * self.__size
