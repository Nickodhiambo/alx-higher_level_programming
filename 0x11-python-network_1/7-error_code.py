#!/usr/bin/python3
"""Evaluates HTTP error in response"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    # Make a GET request and retrieves the response
    response = requests.get(url)

    # Evaluate error
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
