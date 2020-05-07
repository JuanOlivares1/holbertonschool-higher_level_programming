#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        temp = 0
        for k, v in a_dictionary.items():
            if v > temp:
                temp = v
                best = k
        return best
