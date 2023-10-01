#!/usr/bin/python3
"""Sends a POST request to a URL with an email passed as parameter"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Set up email parameter
    data = {'email': email}

    # Make a POST request to URL
    response = requests.post(url, data=data)
    print(response.text)
