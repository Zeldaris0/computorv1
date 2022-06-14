#!/usr/bin/python
import re

class Term_poandco:
    def __init__(self, term):
        self._coef = self.coef_H(term)
        self._power = self.power_H(term)

    def power_H(self, term):
        if re.search('x|X',term):
            if re.search('\^', term):
                indx = re.search('\^', term)
                indx = indx.start()
                if indx > 0 and term[indx+1] !=  "-":
                    return term[indx+1]
                elif indx > 0:
                    power = term[indx+1] + term[indx+1]
                    return power
            else:
                return 1


        else:
            return 0
    
    def coef_H(self, term):
        if re.search("(?<!(\^))[0-9]", term):
            indx = re.search("(?<!(\^))[0-9]", term)
            indx = indx.start()
            return term[indx]
        else:
            return 1

    def get_power(self):
        return self._power

    def get_coef(self):
        return self._coef

