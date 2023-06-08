#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the number of and list of arguments."""
    import sys

    index = len(sys.argv) - 1

    if index == 0:
        print("0 arguments.")
    elif index == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(index))
    for n in range(index):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))
