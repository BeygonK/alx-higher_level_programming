#!/bin/bash
# This script takes a URL, sends request and displays
# the size of the body of response using curl
curl -sI "$url" | grep -i '^Content-Length:' | awk '{print $2}'
