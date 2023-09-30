#!/usr/bin/python3
"""Makes a POST request to a url"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Set up email parameter
    data = {'email': email}

    # Encode POST data
    encoded_data = urllib.parse.urlencode(data).encode('ascii')

    # Make a POST request
    with urllib.request.urlopen(url, data=encoded_data) as response:
        # Decode response body in utf-8
        print(response.read().decode('utf-8'))
