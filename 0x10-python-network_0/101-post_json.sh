#!/bin/bash
# Sends a POST request to a URL in json format
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
