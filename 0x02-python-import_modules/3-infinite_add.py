#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 0
    length = len(sys.argv) - 1
    for i in range (length):
        count += int(sys.argv[i + 1])
    print(count)
