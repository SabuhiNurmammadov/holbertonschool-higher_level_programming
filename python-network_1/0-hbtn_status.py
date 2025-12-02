#!/usr/bin/python3
"""Task 0"""


import urllib.request


url = 'https://intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read() # bu bytes qaytarir
    print("Body response:")
    print(f"\t- type: {type(body)}") 
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode("urf-8")}") #utf-8 
