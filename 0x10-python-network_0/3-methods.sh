#!/usr/bin/bash
# Takes a URL method and retrieves all the requests the server would accept
curl -Is "$1" | grep Allow | cut -c 8-
