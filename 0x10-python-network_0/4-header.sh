#!/bin/bash
# Sends a GET request to a server and sets a header key-value pair
curl -sH "X-School-User-Id: 98" "$1"
