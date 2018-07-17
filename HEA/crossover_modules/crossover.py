from random import randint
from core import Pose

def onePointcrossover(eaObj, inParent):

    #Select a random crossover point on the protein

    randParentLocation = randint(1, len(eaObj.population))
    randParent = eaObj.population[randParentLocation][0]
    while (randParent.sequence() == inParent.sequence()):
        randParentLocation = randint(1, len(eaObj.population))
        randParent = eaObj.population[randParentLocation][0]
    crossOverPoint = randint(1, len(eaObj.population))

    child = Pose()
    child.assign(randParent)

    #We should switch the values from the parents

    for i in range(1, crossOverPoint):
        child.replace_residue(residue(inParent,i))
        
    return child

        
    # Get random number for crossoverpoint.
    # Get random parent from population, ensure that we didn't get the same one.
    # create new Pose object to add to population. (This means that we'll probably have to pass through tPoses from core.py)
    # When we create the new pose, we should duplicate with one of the parents to save some time.

    # Based on the API i've read through, I don't see any methods that could make this easy so here's a solution:
    # We iterate through the size of the crossover point (since we already have one of the parents copied).
    # we utilize "replace_residue" and "residue" to extract each individual strand of residue from a parent and copy it
    # over to the offspring. WARNING: be sure not to copy over the part that has already been copied from 4 lines above.
    # We do this one by one until the offspring has reached it's crossoverpoint and we should have a fully newborn
    # offspring by the end of the loop.

    # Here we just add the newly created pose to tPoses and finish.

    # Alternate solution: you can just return the newly created offspring and do something like this in core.py:
    # tPoses.append(crossover.onePointCrossover(self, tempPose))

def twoPointcrossover(eaObj, inparent): #
    randParentLocation = random.randint(1, len(eaObj.population))
    randParent = eaObj.population[randParentLocation][0]
    while (randParent.sequence() == inParent.sequence()):
        randParentLocation = random.randint(1, len(eaObj.population))
        randParent = eaObj.population[randParentLocation][0]
    crossOverPoint = random.randint(1, len(eaObj.population))

    child = Pose()
    child.assign(randParent)

    #We should switch the values from the parents

    for i in range(1, crossOverPoint):
        child.replace_residue(residue(parent2,i))
        
    return child

def homologousonePointcrossover(eaObj, parents): #could use a parents list

    #Select a random crossover point on the protein

    randParentLocation = random.randint(1, len(eaObj.population))
    randParent = eaObj.population[randParentLocation][0]
    while (randParent.sequence() == inParent.sequence()):
        randParentLocation = random.randint(1, len(eaObj.population))
        randParent = eaObj.population[randParentLocation][0]
    crossOverPoint = random.randint(1, len(eaObj.population))

    child = Pose()
    child.assign(randParent)

    #We should switch the values from the parents

    for i in range(1, crossOverPoint):
        child.replace_residue(residue(parent2,i))
        
    return child

