#!/usr/bin/python3

if __name__ == "__main___":
    import sys

    total = 0
    for i in rangelen((sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
