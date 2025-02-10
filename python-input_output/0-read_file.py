#!/usr/bin/python3
"""
This module defines a function to read and print the contents of a file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8 encoding) and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read.
        Defaults to an empty string.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the file cannot be accessed
        due to permission issues.
    """
    with open(filename, encoding="utf-8") as f:
        text = f.read()
    print(text, end='')
