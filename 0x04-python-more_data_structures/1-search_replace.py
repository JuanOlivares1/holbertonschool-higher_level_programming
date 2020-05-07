#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        new = list(map(
            lambda item: replace if item == search else item,
            my_list))
        return new
