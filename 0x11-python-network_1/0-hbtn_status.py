#!/usr/bin/python3
"""Fetches the URL https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    # Fetch the url
    with urllib.request.urlopen(url) as response:
        # Decode response body
        response_body = response.read()

        # Format response body with tabulation
        print("Body response:")
        print("\t- type: {}".format(type(response_body)))
        print("\t- content: {}".format(response_body))
        print("\t- utf8 content: {}".format(response_body.decode('utf-8')))
