#!/usr/bin/python3
for x in range(10):
    for y in range(x+1, 10):
        if x < 8:
            print(f"{x}{y},", end=" ")
        else:
            print(f"{x}{y}")
