#!/usr/bin/python3
"""Retrieves header info using requests package"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print(dict(response.headers).get("X-Request-Id"))
