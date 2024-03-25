#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        result = list(map(lambda y: y ** 2, x))
        new_matrix.append(result)
    return new_matrix
