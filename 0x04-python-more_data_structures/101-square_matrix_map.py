#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda li: list(map(lambda i: i ** 2, li)), matrix))
