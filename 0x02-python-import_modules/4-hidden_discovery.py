#!/usr/bin/python3

if __name__ == "__main__":
    """Prints all names defined by hidden_4 compiled module."""
    import hidden_4

    names = dir(hidden_4)
    for item in names:
        if item[:2] != "__":
            print(item)
