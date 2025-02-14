#!/usr/bin/python3
"""
This module defines a `Student` class with attributes and methods
to convert its instances into a dictionary representation and update them
from a dictionary.
"""


class Student:
    """
    A class representing a student with basic attributes.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        to_json(self, attrs=None):
            Returns a dictionary representation of the instance.
            If `attrs` is a list of attribute names, only those attributes
            will be included in the output.

        reload_from_json(self, json):
            Replaces the attributes of the instance
            with values from a dictionary.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of the Student instance.

        Args:
            attrs (list, optional): A list of attribute names to include
                                    in the dictionary. Defaults to None.

        Returns:
            dict: A dictionary containing the student's attributes.
                  If `attrs` is provided, only the specified attributes
                  are included if they exist.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {key: getattr(self, key) for key in attrs
                    if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Updates the attributes of the Student instance from a dictionary.

        Args:
            json (dict): A dictionary containing new attribute values.

        This method replaces the instance attributes with the values provided
        in the `json` dictionary, if they exist.
        """
        for key, value in json.items():
            setattr(self, key, value)
