#!/usr/bin/python3
"""Defines a function that creates a string object from a JSON file"""
import json


def load_from_json_file(filename):
    """Creates a string object from a json file"""
    with open(filename) as f:
        return json.load(f)
