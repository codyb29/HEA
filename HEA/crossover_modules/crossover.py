from random import randint
# TODO: find a more specific path for the "compare_atom_coordinates"
# Below is just a quick fix to get things working.
from pyrosetta import *
from rosetta import *
# from core import Pose
import random


def onePointcrossover(eaObj, inParent):
    # Get random number for crossoverpoint.
    randParentLocation = randint(1, len(eaObj.population) - 1)
    # Get random parent from population, ensure that we didn't get the same one.
    randParent = eaObj.population[randParentLocation][0]

    while (core.pose.compare_atom_coordinates(randParent, inParent)):
        randParentLocation = randint(1, len(eaObj.population)-1)
        randParent = eaObj.population[randParentLocation][0]

    # Pick a random point in the sequence of the strand of amino acids to crossover
    crossOverPoint = randint(1, eaObj.seqlen)

    # Create a new pose to be crossover'd by the two parents
    child = Pose()
    child.assign(inParent)

    """
    Based on the API i've read through, I don't see any methods that could make this easy so here's a solution:
    We iterate through the size of the crossover point (since we already have one of the parents copied).
    we utilize "replace_residue" and "residue" to extract each individual strand of residue from a parent and copy it
    over to the offspring. WARNING: be sure not to copy over the part that has already been copied from 6 lines above.
    We do this one by one until the offspring has reached it's crossoverpoint and we should have a fully newborn
    offspring by the end of the loop.
    """
    for residue in range(1, crossOverPoint):
        Pose.replace_residue(
            child, residue, Pose.residue(randParent, residue), True)

    return child


"""
Implemented very similarly to the one-point crossover because they are inherently very similar in theory. Therefore,
minimal documentation is necessary.
"""


def twoPointcrossover(eaObj, inParent):
    # Random selection for the necessary components.
    randParentLocation = randint(1, len(eaObj.population)-1)
    randParent = eaObj.population[randParentLocation][0]

    # Maybe a do-while would do the trick to solve the equality problem?
    crossOverPoint1 = randint(1, len(eaObj.population))
    crossOverPoint2 = randint(1, len(eaObj.population))
    # the first crossover point should be smaller than the second one.
    # TODO: This can be implemented more effectively.
    while(crossOverPoint1 >= crossOverPoint2):
        crossOverPoint1 = randint(1, len(eaObj.population))
        crossOverPoint2 = randint(1, len(eaObj.population))

    # The crossover'd child
    child = Pose()
    child.assign(randParent)

    # We switch the values between the two crossover points with values from the second parent
    for residue in range(crossOverPoint1, crossOverPoint2):
        Pose.replace_residue(
            child, residue, Pose.residue(inParent, residue), True)

    # Alternatively, we should switch the values from the parents two times consecutively
    '''for i in range(1, crossOverPoint1):
        Pose.replace_residue(child, i, Pose.residue(inParent,i), True)
    
    for i in range(1, crossOverPoint2):
        Pose.replace_residue(child, i, Pose.residue(inParent,i), True)'''

    return child


"""
Implements the homologous one point crossover. Randomly selects from a set of points in a chain of residue that are
of similarity between two parents as a crossover point. Then proceeds to replace the portion selected. 
"""


def homologousonePointcrossover(eaObj, inParent):
    # Random selectdion for necessary components
    randParentLocation = randint(1, len(eaObj.population)-1)
    randParent = eaObj.population[randParentLocation][0]

    child = Pose()
    child.assign(randParent)
    similarpoints = []  # Creating a list to store points with similar angles found

    # Searching for similar angles
    for i in range(1, len(inParent)):
        if((child.phi(i) == randParent.phi(i)) and (child.psi(i) == randParent.psi(i)) and (child.chi(i) == randParent.chi(i))):
            similarpoints.append(i)

    # Now we select a random point from the list of points that had similar angles as our crossOverPoint
    crossOverPoint = random.choice(similarpoints)

    # We should switch the values from the parents
    for residue in range(1, crossOverPoint):
        Pose.replace_residue(
            child, residue, Pose.residue(inParent, residue), True)

    return child
