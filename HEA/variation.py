import variation_modules as variation
from math import inf

def perturb(eaObj, posePair):
    if eaObj.cfg['variation']['fragReplacement'] == '1':
        posePair[1] = variation.fragReplace(eaObj, posePair[0])
        eaObj.evalnum += 1
