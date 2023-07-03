#!/usr/bin/python3
"""Supplies the function text_indentation"""


def text_indentation(text):
    """Prints text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ch = 0
    while ch < len(text) and text[ch] == ' ':
        ch += 1

    while ch < len(text):
        print(text[ch], end="")
        if text[ch] == "\n" or text[ch] in ".?:":
            if text[ch] in ".?:":
                print("\n")
            ch += 1
            while ch < len(text) and text[ch] == ' ':
                ch += 1
            continue
        ch += 1
