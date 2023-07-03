#!/usr/bin/python3
""" This module supplies the function matrix_divided"""


def matrix_divided(matrix, div):
    """This function divides all elemment of matrix by div"""
    for i in matrix:
        for j in i:
            if (not isinstance(j, int) and
                    not isinstance(j, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_size = len(matrix[0])
    
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
    if (not isinstance(div, int) and
            not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            result = num / div
            result_rounded = round(result, 2)
            new_row.append(result_rounded)
        new_matrix.append(new_row)
    return (new_matrix)
