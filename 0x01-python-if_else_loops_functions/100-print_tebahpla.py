#!/usr/bin/python3
for c in range(122, 96, -1):
    if c % 2:
        print("{}".format(chr(c - 32)), end="")
        continue
    print("{}".format(chr(c)), end="")
