#!/usr/bin/python3
"""
Module for converting a CSV file to JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to JSON and writes the output to `data.json`.

    Args:
        csv_filename (str): The name of the CSV file to convert.

    Returns:
        bool: True if the conversion is successful, False otherwise.

    Raises:
        FileNotFoundError: If the specified CSV file does not exist.
        Exception: For any other errors that may occur during file processing.
    """
    try:
        # Open the CSV file
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        # Write the data to a JSON file
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: File {csv_filename} not found.")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
