#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    a = 10
    b = 5
    t = add(a, b)
    d = sub(a, b)
    p = mul(a, b)
    q = div(a, b)
    print("{} + {} = {}".format(a, b, t))
    print("{} - {} = {}".format(a, b, d))
    print("{} * {} = {}".format(a, b, p))
    print("{} / {} = {}".format(a, b, q))
