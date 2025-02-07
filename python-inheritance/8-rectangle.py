#!/usr/bin/python3

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


"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""


class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle, inheriting from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes the Rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
