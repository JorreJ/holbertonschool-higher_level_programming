#!/usr/bin/python3
"""
Module: my_list
Defines a class `MyList` that extends the built-in `list` class
and adds a method to print the list in sorted order.
"""


class MyList(list):
    """
    A subclass of the built-in `list` that provides an additional method
    to print the list in sorted order.

    Methods:
        print_sorted(self):
            Prints the list in ascending sorted order without modifying 
            the original list.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.

        The original list remains unchanged.
        """
        print(sorted(self))
