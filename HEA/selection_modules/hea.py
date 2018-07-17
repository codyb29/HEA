
def hea(eaObj):
    return eaObj.population


def truncate(eaObj, prevPop, nextPop):
    # Sort the previous population and next population based on scores.
    prevPop = sorted(prevPop, key=lambda conformation: conformation[1])
    nextPop = sorted(nextPop, key=lambda conformation: conformation[1])

    maxPopulation = len(prevPop)
    prevElite = int(maxPopulation * 0.25)
    nextElite = maxPopulation - prevElite
    return prevPop[ : prevElite] + nextPop[ : nextElite]
