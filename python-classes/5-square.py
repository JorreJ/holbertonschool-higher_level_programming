#!/usr/bin/python3
"""
Module: square
Defines a class Square that represents a square.

This module introduces a basic class definition in Python, serving as a
template for creating square objects. The class includes a private attribute
to store the size of the square and ensures that the size follows specific
validation rules. It also provides methods to retrieve and update the size
safely using property decorators, calculate the square's area, and print
a visual representation of the square using the '#' character.
"""


class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square, stored as a private attribute.

    Properties:
        size (int): Getter and setter for the square's size,
        ensuring valid values.

    Methods:
        __init__(self, size=0): Initializes a square with a given size,
                                ensuring it is a non-negative integer.
        area(self): Returns the area of the square.
        my_print(self): Prints the square using the '#' character.
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
            The size attribute is private and should be accessed through
            the getter and setter methods.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Setter method for updating the size of the square.

        Args:
            size (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
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

    def my_print(self):
        """
        Prints the square using the '#' character.

        If the size is 0, prints an empty line.
        Otherwise, prints a grid of '#' characters of dimensions size x size.
        """
        if self.__size == 0:
            print('')
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end='')
                print('')
