#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ Squares the integers of a matrix"""

    new_matrix = matrix.copy()

    for item in range(len(matrix)):
        new_matrix[item] = list(map(lambda x: x**2, matrix[item]))

    return (new_matrix)
