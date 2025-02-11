#!/usr/bin/python3
"""
This module defines a function to convert a JSON string to a Python object.
"""

import json


def from_json_string(my_str):
    """
    Converts a JSON-formatted string into a Python object.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The corresponding Python object.
    """
    return json.loads(my_str)
