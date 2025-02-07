#!/usr/bin/env python3
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width * 2) + (self.__height * 2)

class Circle(Shape):

    def __init__(self, radius):
        self.__radius = abs(radius)

    def area(self):
        return pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * pi * self.__radius

def shape_info(shape):
    print(f"Area: {shape.area()}\nPerimeter: {shape.perimeter()}")
