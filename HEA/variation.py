import variation_modules as variation

def perturb(eaObj, childData):
    if eaObj.cfg['variation']['fragReplacement'] == '1':
        childData.score = variation.fragReplace(eaObj, childData.pose)
        eaObj.evalnum += 1
