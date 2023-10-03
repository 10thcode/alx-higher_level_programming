#!/usr/bin/python3
'''
list 10 commits of the repository “rails” by the user “rails”
'''
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    username = "10thcode"
    password = "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"
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    auth = requests.auth.HTTPBasicAuth(username, password)
    response = requests.get(url)
    body = response.json()
    i = 0
    for commit in body:
        if i < 10:
            sha = commit.get("sha")
            author = commit.get("commit").get("author").get("name")
            print("{}: {}".format(sha, author))
            i += 1
