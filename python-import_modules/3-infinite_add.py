#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = 0
    for x in range(len(sys.argv) - 1):
        a += int(sys.argv[x + 1])
    print(a)
