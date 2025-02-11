#!/usr/bin/python3
"""
This module defines a function to convert a Python object to a JSON string.
"""

import json


def to_json_string(my_obj):
    """
    Converts a Python object into a JSON-formatted string.

    Args:
        my_obj: The Python object to be converted to JSON.

    Returns:
        str: The JSON representation of `my_obj`.
    """
    return json.dumps(my_obj)
