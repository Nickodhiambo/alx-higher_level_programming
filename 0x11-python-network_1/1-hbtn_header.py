#!/usr/bin/python3
""" Sends a GET request to a URL and retrieves header info"""

import sys
import urllib.request

if __name__ == "__main__":
    # Get URL from command line
    url = sys.argv[1]

    # Fetch url
    with urllib.request.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
