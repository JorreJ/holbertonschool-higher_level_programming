#!/usr/bin/python3
"""
This script adds command-line arguments to a list
and saves them to a JSON file.

Functionality:
- Loads an existing list from `add_item.json` (if the file exists).
- Adds new command-line arguments to the list.
- Saves the updated list back to `add_item.json`.

Modules:
- sys: Used to access command-line arguments.
- save_to_json_file: Saves a Python object to a JSON file.
- load_from_json_file: Loads a Python object from a JSON file.

Usage:
    ./7-add_item.py arg1 arg2 ...
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Attempt to load the existing list from the file
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add new arguments to the list
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, filename)
