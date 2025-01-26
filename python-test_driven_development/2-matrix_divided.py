#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains a function that divides all elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number,
    and returns a new matrix with the results rounded to 2 decimal places.

    Args:
        matrix (list of list of int/float): The matrix to be divided.
        div (int/float): The divisor.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.

    Returns:
        list of list of float: A new matrix with the division results.
    """
    invalid_mat = "matrix must be a matrix (list of lists) of integers/floats"

    # Check if matrix is a non-empty list
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(invalid_mat)

    # Check if matrix is a list of lists and no row is empty
    if not all(isinstance(row, list) for row in matrix) or any(
            len(row) == 0 for row in matrix):
        raise TypeError(invalid_mat)

    # Check if each element is an integer or a float
    if not all(isinstance(element, (int, float))
               for row in matrix for element in row):
        raise TypeError(invalid_mat)

    # Check if all rows have the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division and round results to 2 decimal places
    return [[round(element / div, 2) for element in row] for row in matrix]
