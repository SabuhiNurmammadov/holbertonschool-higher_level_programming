#!/usr/bin/python3
"""Task 4"""


import request

if __name__ == Æ"__main__":
    url = "https://intranet.hbtn.io/status"
    req = request.get(url)
    body = req.text
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
