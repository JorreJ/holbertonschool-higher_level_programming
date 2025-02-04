#!/usr/bin/python3
"""
Module: lookup
Defines a function `lookup` that returns the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of the given object.

    Args:
        obj (any): The object whose attributes and methods will be retrieved.

    Returns:
        list: List containing the names of all attributes and methods of `obj`.
    """
    return dir(obj)
