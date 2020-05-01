#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argnum = len(argv)
    if argnum != 4:
        print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
        exit(1)
    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])
    if op == "+":
        foo = add(a , b)
    elif op == "-":
        foo = sub(a, b)
    elif op == "*":
        foo = mul(a, b)
    elif op == "/":
        foo = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    string = "{:d} {} {:d} = ".format(a, op, b)
    print("{:s} {:d}".format(string, foo))
