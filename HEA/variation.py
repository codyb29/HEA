import variation_modules as variation

def perturb(eaObj, posePair):
    if eaObj.cfg['variation']['fragReplacement'] == '1':
        posePair[1] = variation.fragReplace(eaObj, posePair[0])
        eaObj.evalnum += 1
