#!/usr/bin/python3
"""
This module defines the `BaseGeometry` class.
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
