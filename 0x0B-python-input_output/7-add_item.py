#!/usr/bin/python3
"""Implements load, add and save using json"""
import sys
if __name__ == "__main__":
    load_from_json_file = \
            __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

my_list = load_from_json_file("add_item.json")
my_list = []
my_list.extend(sys.argv[1:])
save_to_json_file(my_list, "add_item.json")
