#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me
curl -sX PUT -d user_id=98 -H "Origin: School" 0.0.0.0:5000/catch_me_2 -L
