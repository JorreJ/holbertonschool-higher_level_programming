#!/usr/bin/python3
"""
This module defines a function to write text to a file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8 encoding)
    and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        Defaults to an empty string.
        text (str): The text to write into the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
