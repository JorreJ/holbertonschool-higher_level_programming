#!/usr/bin/python3
"""
This module defines a function to save a Python object
to a file in JSON format.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a file using JSON representation.

    Args:
        my_obj: The Python object to serialize.
        filename (str): The name of the file where
        the JSON data will be stored.

    Returns:
        None
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
