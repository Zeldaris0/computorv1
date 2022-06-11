#!/usr/bin/python

import sys
import re

def sign_cleaner(term_list):
    termlen = len(term_list)
    for idx, term in enumerate(term_list):
        if term == "-" and idx < termlen-1:
            term_list[idx+1] = "-" + term_list[idx+1]
            term_list[idx] = None
    
    term_list = filter(None, term_list)
    return term_list


def parser(poly):
    poly = poly.replace(" ", "")
    allowed = "0123456789-+*^xX"
    if not all(c in allowed for c in poly):
        print("ERROR404")
        return 0

    poly = re.sub("-\+|\+-", "-", poly)
    poly = re.sub("--", "+", poly)
    poly_splited = re.split("(?<!\*)([-])|(?<!\*)\+", poly)
    poly_splited = filter(None, poly_splited)
    term_list = sign_cleaner(poly_splited)
    print (term_list)


def main():
    if (len(sys.argv) > 2):
        print ("there is more that 1 arg")
        return 0
    else:
        arr = str(sys.argv[1])
        arr = arr.split("=")
        if len(arr) != 2:
            print("ERROR4044")
            return 0
        poly1 = parser(arr[0])
        poly2 = parser(arr[1])

if __name__ == "__main__":
    main()