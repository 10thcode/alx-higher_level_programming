#!/bin/bash
# sends a GET request to a URL, and displays the body of the response
curl -s -H "X-School-User-Id:98" -X GET $1
