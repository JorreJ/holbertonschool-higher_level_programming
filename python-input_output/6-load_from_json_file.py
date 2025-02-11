#!/usr/bin/python3
"""
This module defines a function to load a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Reads a JSON file and returns the corresponding Python object.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        object: The Python object deserialized from the JSON file.
    """
    with open(filename) as f:
        return json.load(f)
