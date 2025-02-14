#!/usr/bin/python3
"""
This module provides functions for serializing data to a JSON file
and deserializing data from a JSON file.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes Python data into JSON format and saves it to a file.

    Args:
        data (any): The Python object to be serialized (must be JSON serializable).
        filename (str): The name of the file where the data will be saved.

    This function writes the JSON representation of `data` to the specified file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        any: The deserialized Python object from the JSON file.

    This function reads the JSON data from the specified file and converts it
    back into a Python object.
    """
    with open(filename) as f:
        return json.load(f)
