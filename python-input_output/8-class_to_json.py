#!/usr/bin/python3
"""
This module defines a function to convert a class instance
into a dictionary representation for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of an object's attributes
    for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary containing all attributes of the object.
    """
    return obj.__dict__
