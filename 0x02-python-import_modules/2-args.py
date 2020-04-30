#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    string, strarg = "", ""
    if length == 1:
        string = "0 arguments."
    elif length == 2:
        string = "1 argument:"
        strarg = "1: {}\n".format(argv[1])
    else:
        string = "{} arguments:".format(length - 1)
        for i in range(1, length):
            strarg += "{}: {}\n".format(i, argv[i])
    print(string)
    print(strarg, end="")
