#!/bin/bash
# Send a POST request and displays response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"