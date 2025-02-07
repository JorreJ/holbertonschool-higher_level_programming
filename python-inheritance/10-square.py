#!/usr/bin/python3
"""
This module defines the `Square` class, which inherits from `Rectangle`.
"""

# Importing Rectangle from another module
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that represents a square, inheriting from Rectangle.

    Attributes:
        __size (int): The size of the square (private attribute).

    Methods:
        __init__(self, size):
            Initializes a square with a validated size.
    """

    def __init__(self, size):
        """
        Initializes the Square with a given size.

        Args:
            size (int): The size of the square (both width and height).

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is not greater than 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
