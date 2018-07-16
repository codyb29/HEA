import crossover_modules as crossover

def typeofcrossover(eaObj, pose):
    if eaObj.cotype == 1:
        crossover.onePointcrossover(eaObj, pose)
        
    elif eaObj.cotype == 2:
        crossover.twoPointcrossover(eaObj, pose)

    elif eaObj.cotype == 3:
        crossover.homologousonePointcrossover(eaObj, pose)
