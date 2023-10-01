#!/usr/bin/python3
"""Sends a GET request to Github API"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Github API url
    url = 'https://api.github.com/user'

    username = sys.argv[1]
    password = sys.argv[2]

    # Authenticate the user
    auth = HTTPBasicAuth(username, password)

    # Make a GET request to the API
    response = requests.get(url, auth=auth)

    # Display user id
    print(response.json().get("id"))
