#!/usr/bin/python3
"""
This module defines a function to check if an object is an instance of,
or inherits from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or inherits from, a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or a subclass of a_class,
        otherwise False.
    """
    return isinstance(obj, a_class)
