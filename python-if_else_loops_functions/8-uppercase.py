#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if x >= 'a' and x <= 'z':
            char = chr(ord(x) - 32)
        else:
            char = x
        print(char, end="")
    print("")
