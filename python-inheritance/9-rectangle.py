#!/usr/bin/python3
"""
This module defines the `Rectangle` class, which inherits from `BaseGeometry`.
"""

# Importing BaseGeometry from another module
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle, inheriting from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle (private attribute).
        __height (int): The height of the rectangle (private attribute).

    Methods:
        __init__(self, width, height):
            Initializes a rectangle with validated width and height.

        area(self):
            Computes and returns the area of the rectangle.

        __str__(self):
            Returns a formatted string representation of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If `width` or `height` is not an integer.
            ValueError: If `width` or `height` is not greater than 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            int: The calculated area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the Rectangle.

        Returns:
            str: A formatted string in the format `[Rectangle] width/height`.
        """
        return f"[{type(self).__name__}] {self.__width}/{self.__height}"
