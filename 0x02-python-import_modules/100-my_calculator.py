#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    counter = len(sys.argv) - 1
    if counter != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    opr = {'+': add, '-': sub, '*': mul, '/': div}
    if sys.argv[2] not in opr:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, opr[sys.argv[2]](a, b)))
