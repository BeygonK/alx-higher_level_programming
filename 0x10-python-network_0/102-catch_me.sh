#!/bin/bash
# Make request to url and makes server respond
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -d "user_id=98" -H "Origin:School"
