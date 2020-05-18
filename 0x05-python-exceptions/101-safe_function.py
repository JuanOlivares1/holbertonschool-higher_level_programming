#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    res = None
    try:
        res = fct(*args)
    except Exception as ex:
        print("Exception: {}".format(ex), file=stderr)
    finally:
        return res
