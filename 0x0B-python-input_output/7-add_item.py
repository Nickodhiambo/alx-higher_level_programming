#!/usr/bin/python3
"""Implements load, add and save."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    arguments = sys.argv[1:]
    argument_list = []
    for argument in arguments:
        argument_list.append(argument)
    load_from_json_file("add_item.json")
    for argument in argument_list:
        save_to_json_file(argument, "add_item.json")
