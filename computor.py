#!/usr/bin/python

import sys
import re


def my_function(poly):
    poly_splited = re.split('- |+', poly)
    print (poly_splited)
    for x in poly_splited:
        powerindex = x.find("^")
        if x[powerindex + 1].isdigit():
            if x[powerindex + 1] > 2:
                return 0
        else:
            return 0
    print("Hello from a function")
    return 1

def main():
    if (len(sys.argv) > 2):
        print "there is more that 1 arg"
        return 0
    else:
        degree = my_function(str(sys.argv[1]))

if __name__ == "__main__":
    main()