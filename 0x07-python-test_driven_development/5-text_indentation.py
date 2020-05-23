#!/usr/bin/python3
"""Module
"""


def text_indentation(text):
    """Function
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    res = ""
    f = 0
    for i in text:
        if i in [".", "?", ":"]:
            res += i
            res += "\n\n"
            f = 1
            continue
        if f == 1:
            f = 0
            if i == " ":
                continue
        res += i
    print(res, end="")
