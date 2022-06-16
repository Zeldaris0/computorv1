#!/usr/bin/python
import re

class Term_poandco:
    def __init__(self, term):
        self._coef = self.coef_H(term)
        self._power = self.power_H(term)
        self._all = [self._coef, self._power]

    def power_H(self, term):
        if re.search('x|X',term):
            if re.search('\^', term):
                indx = re.search('\^', term)
                indx = indx.start()
                power = ''

                if term[indx+1] !=  "-":
                    indx = indx + 1
                    for number in term[indx:]:
                        if number.isdigit():
                            power = power + number
                        else:
                            break
                    return power

                else:
                    power = term[indx+1]
                    indx = indx + 2
                    for number in term[indx:]:
                        if number.isdigit():
                            power = power + number
                        else:
                            break
                    return power
            else:
                return 1


        else:
            return 0
    
    def coef_H(self, term):
        if re.search("(?<!(\^))[0-9]", term):
            indx = re.search("(?<!(\^))[0-9]", term)
            indx = indx.start()
            if indx != 0:
                if term[indx-1] == '-':
                    coef = '-'
                else:
                    coef = ''
            else:
                coef = ''
            for number in term[indx:]:
                if number.isdigit():
                    coef = coef + number
                else:
                    break
            return coef
        else:
            return 1

    def get_power(self):
        return self._power

    def get_coef(self):
        return self._coef

