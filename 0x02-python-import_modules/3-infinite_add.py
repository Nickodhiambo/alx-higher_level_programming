#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the result addition of all arguments."""
    import sys

    summation = 0
    for n in range(len(sys.argv) - 1):
        summation += int(sys.argv[n + 1])
    print("{}".format(summation))
