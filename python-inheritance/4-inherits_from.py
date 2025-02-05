#!/usr/bin/python3
"""
This module defines a function to check if an object is a subclass instance
but not a direct instance of a specified class.
"""


def inherits_from(obj, a_class):
    """
    Determines if an object is an instance of a subclass of a given class,
    but not a direct instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a subclass of a_class
        (but not a_class itself), otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
