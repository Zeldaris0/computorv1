#!/usr/bin/python

import sys
import re
from termsC import Term_poandco

def sign_cleaner(term_list):
    termlen = len(term_list)
    for idx, term in enumerate(term_list):
        if term == "-" and idx < termlen-1:
            term_list[idx+1] = "-" + term_list[idx+1]
            term_list[idx] = None
    
    term_list = list(filter(None, term_list))
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
    poly_splited = list(filter(None, poly_splited))
    term_list = sign_cleaner(poly_splited)
    return term_list


def terms_corr(poly1, poly2):
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

def classuser(poly):
    claHolder = []
    for term in poly:
        obj = Term_poandco(term)
        claHolder.append(obj._all)
    claHolder.pop()
    claHolder.sort(key = lambda claHolder: int(claHolder[1]))
    return (claHolder)

def simplifier(Apoly):
    llen = len(Apoly) - 1
    i = 0
    indxl = []
    while i < llen:
        if i >= llen:
            break
        if Apoly[i][1] == Apoly[i + 1][1]:
            Apoly[i + 1][0] = int(Apoly[i + 1][0]) + int(Apoly[i][0])
            indxl.append(i)
        i += 1
    Apoly = [i for j, i in enumerate(Apoly) if j not in indxl]
    return (Apoly)
    

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
    terms_corr(poly1,poly2)
    Spoly_rev(poly2)
    print("---------",poly2)
    Apoly = poly1 + poly2
    print("---------",Apoly)
    Apoly = classuser(Apoly)
    print(Apoly)
    Apoly = simplifier(Apoly)
    print(Apoly)

if __name__ == "__main__":
    main()