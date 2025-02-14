#!/usr/bin/python3
"""
This module defines a `CustomObject` class and provides methods for
serializing and deserializing instances using the `pickle` module.
"""

import pickle


class CustomObject:
    """
    A custom class representing an object with basic attributes.

    Attributes:
        name (str): The name of the object.
        age (int): The age of the object.
        is_student (bool): Indicates whether the object represents a student.

    Methods:
        display():
            Prints the object's attributes in a formatted manner.
        serialize(filename):
            Serializes the object and saves it to a file.
        deserialize(filename):
            Loads a serialized object from a file and returns an instance.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject instance with name, age, and student status.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Whether the object represents a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the object's attributes in a readable format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object and saves it to a file.

        Args:
            filename (str): The name of the file
            where the object will be stored.

        Raises:
            Exception: If an error occurs during serialization.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Loads a serialized object from a file and returns an instance.

        Args:
            filename (str): The name of the file to read from.

        Returns:
            CustomObject or None: The deserialized object,
            or None if an error occurs.

        Raises:
            Exception: If an error occurs during deserialization.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Error deserializing object: {e}")
            return None
