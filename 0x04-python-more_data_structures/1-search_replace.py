#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = list(map(
        lambda item: replace if item == search else item,
        my_list))
    return new
