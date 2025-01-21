#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t = (0,)
    while len(tuple_a) < 2:
        tuple_a += t
    while len(tuple_b) < 2:
        tuple_b += t
    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]
    return (a, b)
