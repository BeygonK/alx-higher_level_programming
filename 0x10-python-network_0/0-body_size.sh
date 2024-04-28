#!/bin/bash
# This script takes a URL, sends request and displays
curl -sI "$url" | grep -i Content-Length | cut -d " " -f 2 
