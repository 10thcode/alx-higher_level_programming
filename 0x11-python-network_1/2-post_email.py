#!/usr/bin/python3
"""
Sends POST request to a URL
"""
from urllib import request
from urllib import parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = parse.urlencode(values).encode("ascii")
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        body = response.read()
        print("{}".format(body.decode("utf-8")))
