from random import randint
from core import Pose
import random

def onePointcrossover(eaObj, inParent):
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

    #Select a random crossover point on the protein

    randParentLocation = randint(1, len(eaObj.population)-1)
    randParent = eaObj.population[randParentLocation][0]
    #while (randParent.sequence() == inParent.sequence()):
    #    randParentLocation = randint(1, len(eaObj.population)-1)
    #    randParent = eaObj.population[randParentLocation][0]
    #Program seems to loop indefinitely here
    crossOverPoint = randint(1, len(eaObj.population))

    child = Pose()
    child.assign(randParent)

    #We should switch the values from the parents
    for i in range(1, crossOverPoint):
        Pose.replace_residue(child, i, Pose.residue(inParent,i), True)
        
    return child

        
   
def twoPointcrossover(eaObj, inParent): #
    randParentLocation = randint(1, len(eaObj.population)-1)
    randParent = eaObj.population[randParentLocation][0]


    crossOverPoint1 = randint(1, len(eaObj.population))
    crossOverPoint2 = randint(1, len(eaObj.population))

    while(crossOverPoint1 >= crossOverPoint2):
        crossOverPoint1 = randint(1, len(eaObj.population))
        crossOverPoint2 = randint(1, len(eaObj.population))


    child = Pose()
    child.assign(randParent)

    #We switch the values between the two crossover points with values from the second parent
    for i in range(crossOverPoint1, crossOverPoint2):
        Pose.replace_residue(child, i, Pose.residue(inParent,i), True)
        

    #Alternatively, we should switch the values from the parents two times consecutively
    '''for i in range(1, crossOverPoint1):
        Pose.replace_residue(child, i, Pose.residue(inParent,i), True)
    
    for i in range(1, crossOverPoint2):
        Pose.replace_residue(child, i, Pose.residue(inParent,i), True)'''
    
    return child

def homologousonePointcrossover(eaObj, inParent):

    randParentLocation = randint(1, len(eaObj.population)-1)
    randParent = eaObj.population[randParentLocation][0]

    child = Pose()
    child.assign(randParent)
    similarpoints = [] #Creating a list to store points with similar angles found

    #Searching for similar angles
    for i in range(1,len(inParent)):
        if(child.phi(i) == randParent.phi(i) and child.psi(i) == randParent.psi(i) and child.chi(i) == randParent.chi(i)):
            similarpoints.append(i)

    #Now we select a random point from the list of points that had similar angles as our crossOverPoint
    crossOverPoint = random.choice(similarpoints)

    #We should switch the values from the parents
    for i in range(1, crossOverPoint):
        Pose.replace_residue(child, i, Pose.residue(inParent,i), True)
        
    return child