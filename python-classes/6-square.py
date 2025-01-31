#!/usr/bin/python3
"""
Module: square
Defines a class Square that represents a square.

This module introduces a basic class definition in Python, serving as a
template for creating square objects. The class includes private attributes
to store the size and position of the square while ensuring specific
validation rules are followed. It also provides methods to retrieve and
update these attributes safely using property decorators, calculate the
square's area, and print a visual representation of the square using the
'#' character with proper positioning.
"""


class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square, stored as a private attribute.
        __position (tuple): A tuple of two positive integers defining the
                            position (x, y) offset when printing the square.

    Properties:
        size (int): Getter and setter for the square's size,
                    ensuring valid values.
        position (tuple): Getter and setter for the square's position,
                          ensuring it is a tuple of two positive integers.

    Methods:
        __init__(self, size=0, position=(0, 0)):Initializes square with a given
                                                size and position ensuring they
                                                meet validation criteria.
        area(self): Returns the area of the square.
        my_print(self): Prints the square using the '#' character, considering
                        its position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with a given size and position.

        Args:
            size (int, optional): The size of the square (default is 0).
            position (tuple, optional): The position of the square,
                                        defined as a tuple of two
                                        positive integers (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
            TypeError: If position is not a tuple of two positive integers.

        Note:
            The size and position attributes are private and should be accessed
            through their respective getter and setter methods.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for updating the size of the square.

        Args:
            size (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for retrieving the position of the square.

        Returns:
            tuple: A tuple of two positive integers representing the position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for updating the position of the square.

        Args:
            value (tuple): A tuple of two positive integers
                        representing the position.

        Raises:
            TypeError: If position is not a tuple of
                    exactly two positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square, calculated as size squared.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using the '#' character, considering its position.

        - If size is 0, prints an empty line.
        - If position is greater than (0, 0),
        the square is indented accordingly.

        Example Output for `size=3, position=(2,1)`:

            (empty line)
            "  ###"
            "  ###"
            "  ###"
        """
        for i in range(self.__position[1]):
            print()
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__position[0]):
                    print(' ', end='')
                for z in range(self.__size):
                    print("#", end='')
                print()
