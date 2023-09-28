#!/bin/bash
# Sends a POST request to a URL and displays message body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
