#!/usr/bin/python3
"""Sends a POST request to a url and displays the response"""

import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    # Letter must be set in the variable q
    data = {'q': letter}

    # Make a POST request to URL
    response = requests.post(url, data=data)

    # Evaluate if response is JSON
    try:
        parsed_response = response.json()

        if parsed_response == {}:
            print("No result")
        else:
            print("[{}] {}".format(parsed_response.get(
                "id"), parsed_response.get("name")))
    except ValueError:
        print("Not a valid JSON")
