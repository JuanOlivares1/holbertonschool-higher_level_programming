#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    res = None
    try:
        res = fct(args[0], args[1])
    except ZeroDivisionError as zde:
        print("Exception: {}".format(zde), file=stderr)
    except IndexError as ie:
        print("Exception: {}".format(ie), file=stderr)
    finally:
        return res
