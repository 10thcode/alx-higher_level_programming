#!/usr/bin/python3
'''
Use GitHub API to display a user id
'''
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    auth = requests.auth.HTTPBasicAuth(username, password)
    response = requests.get("https://api.github.com/user", auth=auth)
    body = response.json()
    print(body.get("id"))
