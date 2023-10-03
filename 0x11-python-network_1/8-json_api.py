#!/usr/bin/python3
"""
Sends a POST request to a URL
"""
import sys
import requests


if __name__ == "__main__":
    q = "" if len(sys.argv) < 2 else sys.argv[1]
    data = {"q": q}
    response = requests.post("http://0.0.0.0:5000/search_user", data)
    try:
        body = response.json()
        if body:
            id = body.get("id")
            name = body.get("name")
            print("[{}] {}".format(id, name))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
