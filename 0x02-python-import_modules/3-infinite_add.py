#!/usr/bin/python3
if __name__ == "__main__":
    """ prints the result of the addition of all arguments """
    import sys
    total = sum(int(arg) for arg in sys.argv[1:])
    print(total)
