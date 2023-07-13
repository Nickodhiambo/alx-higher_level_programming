#!/usr/bin/python3
"""Implements load, add and save."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []
    new_items = sys.argv[1:]
    updated_list = my_list + new_items
    save_to_json_file(updated_list, "add_item.json")
