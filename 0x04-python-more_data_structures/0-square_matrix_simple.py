#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        return [[x ** 2 for x in li] for li in matrix]
