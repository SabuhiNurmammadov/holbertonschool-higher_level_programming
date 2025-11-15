#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            new_str += "{}".format(chr(ord(i) - 32)), end=""
        else:
            new_str += "{}".format(i)
    print("{}".format(new_str))

