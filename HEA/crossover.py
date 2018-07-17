import crossover_modules as crossover

def typeofcrossover(eaObj, pose):
    if eaObj.cotype == 1:
        return crossover.onePointcrossover(eaObj, pose)
        
    elif eaObj.cotype == 2:
        return crossover.twoPointcrossover(eaObj, pose)

    elif eaObj.cotype == 3:
        return crossover.homologousonePointcrossover(eaObj, pose)
