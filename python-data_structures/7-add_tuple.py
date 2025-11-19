#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            touple_a = (0, 0)
        else:
            touple_a = (touple_a[0], 0)
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            touple_b = (0, 0)
        else:
            touple_b = (touple_b[0], 0)
    return (touple_a[0] + touple_b[0], touple_a[1] + touple_b[1])
