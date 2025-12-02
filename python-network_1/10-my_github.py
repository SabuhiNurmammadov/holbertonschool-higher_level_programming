#!/usr/bin/python3
"""Task 9"""


import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    headers = {"Authorization": f"token {sys.argv[2]}"}

    try:
        req = requests.get(url, headers = headers)
        print(reqx.json()['id'])
    except Exception:
        print(None)
