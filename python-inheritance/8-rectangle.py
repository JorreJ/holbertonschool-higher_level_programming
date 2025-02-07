#!/usr/bin/python3
"""
This module defines the `BaseGeometry` and `Rectangle` classes.
"""


class BaseGeometry:
    """
    A class representing geometric shapes.

    Methods:
        area(self):
            Raises an Exception indicating that the method
            is not yet implemented.

        integer_validator(self, name, value):
            Validates that a given value is a positive integer.
    """

    def area(self):
        """
        Raises an Exception to indicate that the area() method
        must be implemented by subclasses.

        Raises:
            Exception: Always raises an error since the method
            is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that `value` is a positive integer.

        Args:
            name (str): The name of the parameter (used in the error message).
            value (int): The value to validate.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle, inheriting from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height):
            Initializes a rectangle with validated width and height.
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
