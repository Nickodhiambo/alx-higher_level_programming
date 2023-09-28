#!/bin/bash
# Takes a URL, sends a request to URL, displays the size of body of response
curl -s "$1" | wc -c
