#!/bin/bash
# This script takes a URL, sends request and displays
curl -sI "$url" | grep -i '^Content-Length:' | awk '{print $2}'
