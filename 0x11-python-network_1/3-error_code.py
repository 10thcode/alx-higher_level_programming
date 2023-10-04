#!/usr/bin/python3
'''
Sends a request to a URL
and display the body of the response.
'''
from urllib import request
from urllib import error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            body = response.read()
            print("{}".format(body.decode("utf-8")))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
