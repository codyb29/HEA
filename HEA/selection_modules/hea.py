
def hea(eaObj):
    return eaObj.population


def truncate(eaObj, prevPop, nextPop):
    # Sort the previous population and next population based on scores.
    prevPop = sorted(prevPop, key=lambda conformation: conformation[1])
    nextPop = sorted(nextPop, key=lambda conformation: conformation[1])

    prevElite = int(len(prevPop) * 0.25) # Select the top 25% of prevPop
    nextPop = nextPop + prevPop[ : prevElite] # Concatenate prevPop with new Pop
    # Sort one more time for both populations to compete with each other.
    nextPop = sorted(nextPop, key=lambda conformation: conformation[1])
    # return the top 100 configurations for the next population
    return nextPop[ : 100]
