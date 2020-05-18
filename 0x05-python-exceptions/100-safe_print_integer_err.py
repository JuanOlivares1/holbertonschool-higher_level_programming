#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as ex:
        print("Exception: {}".format(ex), file=stderr)
        return False
    else:
        return True
