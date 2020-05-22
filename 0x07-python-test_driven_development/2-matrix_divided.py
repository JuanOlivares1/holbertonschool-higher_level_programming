#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(matrix) == list:
        new = []
        for row in matrix:
            new_row = []
            if type(row) != list:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            elif len(row) == len(matrix[0]):
                if type(div) not in [int, float]:
                    raise TypeError("div must be a number")
                    return None
                if div == 0:
                    raise ZeroDivisionError("division by zero")
                    return None
                for i in row:
                    if type(i) not in [int, float]:
                        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                    else:
                        new_row.append(round(i / div, 2))
                new.append(new_row)
            else:
                raise TypeError("Each row of the matrix must have the same size")
    else:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return new
