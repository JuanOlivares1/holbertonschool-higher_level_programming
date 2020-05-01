#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argnum = len(argv) - 1
    if argnum != 3:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)
    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])
    if op == "+":
        foo = add
    elif op == "-":
        foo = sub
    elif op == "*":
        foo = mul
    elif op == "/":
        foo = div
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    string = "{:d} {} {:d} = ".format(a, op, b)
    print("{:s} {:d}".format(string, foo(a, b)))
