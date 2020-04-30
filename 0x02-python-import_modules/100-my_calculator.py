#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argnum = len(argv) - 1
    if argnum < 3:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit (1)
    a, op, b = int(argv[1]), argv[2], int(argv[3])
    if op not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit (1)
    string = "{:d} {} {:d} = ".format(a, op, b)
    for op2, foo in [('+', add), ('-', sub), ('*', mul), ('/', div)]:
        if op == op2:
            print("{:s} {:d}".format(string, foo(a, b)))
