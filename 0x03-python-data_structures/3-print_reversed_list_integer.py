#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        print()
        return
    rev = my_list[:]
    rev.reverse()
    for i in rev:
        print("{:d}".format(i))
