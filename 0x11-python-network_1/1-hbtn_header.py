#!/usr/bin/python3
'''
Sends a request to a URL and display the value of the
X-Request-Id
'''
from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = request.Request(url)
    with request.urlopen(req) as response:
        value = response.headers.get("X-Request-Id")
        print("{}".format(value))
