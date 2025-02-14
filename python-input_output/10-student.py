#!/usr/bin/python3
"""
This module defines a `Student` class with attributes and a method
to convert its instances into a dictionary representation.
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
        if isinstance(attrs, list):
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        return self.__dict__
