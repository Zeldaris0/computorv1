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
    allowed = "0123456789-+*^xX/"
    if not all(c in allowed for c in poly):
        print("ERROR404")
        return 0

    poly = re.sub("-\+|\+-", "-", poly)
    poly = re.sub("--", "+", poly)
    poly_splited = re.split("(?<!(\*|\^|/))([-])|(?<!(\*|\^|/))\+", poly)
    poly_splited = filter(None, poly_splited)
    term_list = sign_cleaner(poly_splited)
    return term_list


def terms_checker(poly1, poly2):
    for i, term in enumerate(poly1):
        poly1[i] = term.replace('+', '')

    for i, term2 in enumerate(poly2):
        poly2[i] = term2.replace('+', '')

def Spoly_rev(poly2):
    for i, term in enumerate(poly2):
        if term[0] == "-":
            term = term[:0] + "" + term[1:]
            poly2[i] = term
        else:
            term = "-" + term
            poly2[i] = term



def main():
    if (len(sys.argv) > 2):
        print ("there is more that 1 arg")
        return 0
    
    arr = str(sys.argv[1])
    arr = arr.split("=")
    if len(arr) > 2:
        print("ERROR4044")
        return 0
    if (len(arr) < 2):
        poly2 = ['0']
        poly1 = parser(arr[0])
    else:
        poly1 = parser(arr[0])
        poly2 = parser(arr[1])
        if poly2 == []:
            poly2 = ['0']
    terms_checker(poly1,poly2)
    Spoly_rev(poly2)
    Apoly = poly1 + poly2
    print (Apoly)

if __name__ == "__main__":
    main()