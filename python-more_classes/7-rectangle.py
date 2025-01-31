#!/usr/bin/python3
"""
Module: rectangle
Defines a class Rectangle that represents a rectangle.

This module introduces a class definition for creating rectangle objects.
The class includes private attributes for width and height, along with
property methods to retrieve and update these attributes while ensuring
proper validation. It also provides methods to calculate the area and
perimeter of the rectangle. Additionally, it includes a string representation
method to visualize the rectangle using a configurable symbol, a representation
method to provide a formal string representation of the rectangle, and a
counter that tracks the number of instances created and deleted.
"""


class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
        number_of_instances (int): A class attribute that tracks the number
            of Rectangle instances created and deleted.
        print_symbol (any): A class attribute used as the symbol for string
            representation of the rectangle.
        __width (int): The width of the rectangle,
        stored as a private attribute.
        __height (int): The height of the rectangle,
        stored as a private attribute.

    Properties:
        width (int): Getter and setter for the rectangle's width,
        ensuring valid values.
        height (int): Getter and setter for the rectangle's height,
        ensuring valid values.

    Methods:
        __init__(self, width=0, height=0):
            Initializes a rectangle with given width and height,
            ensuring they are non-negative integers.
        area(self):
            Returns the area of the rectangle.
        perimeter(self):
            Returns the perimeter of the rectangle.
        __str__(self):
            Returns a string representation of the rectangle
            using `print_symbol`.
        __repr__(self):
            Returns an official string representation of the rectangle
            that can be used to recreate the object.
        __del__(self):
            Prints a message when the rectangle is deleted and decrements
            the instance counter.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with a given width and height.

        Args:
            width (int, optional): The width of the rectangle (default is 0).
            height (int, optional): The height of the rectangle (default is 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.

        Note:
            The width and height attributes are private and should be accessed
            through their respective getter and setter methods.
            The class attribute `number_of_instances` keeps track of how many
            Rectangle instances exist.
            The class attribute `print_symbol` defines the symbol used when
            printing the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle.

        Returns:
            int: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for updating the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is negative.
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Getter method for retrieving the height of the rectangle.

        Returns:
            int: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for updating the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is negative.
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle, calculated as width * height.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle,
            calculated as 2 * (width + height).
                 Returns 0 if either width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Returns a string representation of the rectangle using `print_symbol`.

        If width or height is 0, returns an empty string.
        Otherwise, represents the rectangle as multiple lines of the defined
        `print_symbol`, which can be any character or object.

        Returns:
            str: A visual representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width
                          for _ in range(self.__height)])

    def __repr__(self):
        """
        Returns an official string representation of the rectangle.

        The returned string is in the form of:
            Rectangle(width, height)
        This allows the object to be recreated using eval().

        Returns:
            str: A formal string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message when the rectangle is deleted
        and decrements the instance counter.

        This method is automatically called
        when an instance is garbage collected.
        It also decreases the `number_of_instances` count.

        Prints:
            "Bye rectangle..."
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
