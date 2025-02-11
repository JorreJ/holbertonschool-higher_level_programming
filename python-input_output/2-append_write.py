#!/usr/bin/python3
"""
This module defines a function to append text to a file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8 encoding)
    and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        Defaults to an empty string.
        text (str): The text to append to the file.
        Defaults to an empty string.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
