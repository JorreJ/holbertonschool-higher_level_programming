#!/usr/bin/python3
"""
This module defines the `BaseGeometry` class.
"""


class BaseGeometry:
    """
    A class representing geometric shapes.

    Methods:
        area(self): Raises an Exception indicating that the method
                    is not yet implemented.
    """

    def area(self):
        """
        Raises an Exception to indicate that the area() method
        must be implemented by subclasses.
        """
        raise Exception("area() is not implemented")
