#!/usr/bin/python3
"""Sends a GET request to URL and manages HTTP error"""

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]

    # Send a GET request and handle error
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        # Handles error and displays HTTP status code
        print("Error code: {}".format(e.code))
