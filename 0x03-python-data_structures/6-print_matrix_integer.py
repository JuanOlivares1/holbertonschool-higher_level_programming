#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        string = ""
        for j in i:
            string += "{:d}".format(j)
        print(" ".join(string))
