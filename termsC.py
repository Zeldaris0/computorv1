#!/usr/bin/python
import re

class Term_poandco:
    def __init__(self, term):
        self._coef = self.coef_H(term)
        self._power = self.power_H(term)

    def power_H(term):
        if re.find('x|X',term):
            if re.find('^', term):
                indx = re.find('^', term)
                if term[indx+1] !=  "-":
                    return term[indx+1]
                else:
                    power = term[indx+1] + term[indx+1]
                    return power
            else:
                return 1


        else:
            return 0
    
    def coef_H(term):
        if re.find("(?<!(\^))[0-9]", term):
            indx = re.find("(?<!(\^))[0-9]", term)
            return term[indx]
        else:
            return 1

    def get_power(self):
        return self._power

    def get_coef(self):
        return self._coef

