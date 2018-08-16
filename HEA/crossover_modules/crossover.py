from random import randint
from pyrosetta import Pose
from rosetta import core
import random


def randomParent(eaObj, base):
    while True:
        # Get random number for crossoverpoint.
        uniqueParentLocation = randint(1, len(eaObj.population) - 1)
        # Get random parent from population, ensure that we didn't get the same one.
        uniqueParent = eaObj.population[uniqueParentLocation]
        if (uniqueParent != base):
            break

    return uniqueParent.pose


def onePointcrossover(eaObj, inParent):
    # Get random parent from population, ensure that we didn't get the same one.
    randParent = Pose()
    randParent.assign(randomParent(eaObj, inParent))

    # Pick a random point in the sequence of the strand of amino acids to crossover
    crossOverPoint = randint(1, inParent.pose.size())

    # Create a new pose to be crossover'd by the two parents
    child = Pose()
    child.assign(inParent.pose)

    """
    We iterate through the size of the crossover point (since we already have one of the parents copied)
    one by one until the offspring has reached it's crossoverpoint and we should have a fully newborn
    offspring by the end of the loop.
    """
    for residue in range(1, crossOverPoint):
        Pose.replace_residue(
            child, residue, Pose.residue(randParent, residue), True)

    inParent.pose.assign(child)


"""
Implemented very similarly to the one-point crossover because they are inherently very similar in theory. Therefore,
minimal documentation is necessary.
"""


def twoPointcrossover(eaObj, inParent):
    randParent = Pose()
    randParent.assign(randomParent(eaObj, inParent))

    crossOverPoint1 = randint(1, inParent.pose.size())
    crossOverPoint2 = randint(1, inParent.pose.size())
    # the first crossover point should be smaller than the second one.
    while(crossOverPoint1 >= crossOverPoint2):
        crossOverPoint1 = randint(1, inParent.pose.size())
        crossOverPoint2 = randint(1, inParent.pose.size())

    # The crossover'd child
    child = Pose()
    child.assign(inParent.pose)

    # We switch the values between the two crossover points with values from the random parent
    for residue in range(crossOverPoint1, crossOverPoint2):
        Pose.replace_residue(
            child, residue, Pose.residue(randParent, residue), True)

    inParent.pose.assign(child)


"""
Implements the homologous one point crossover. Randomly selects from a set of points in a chain of residue that are
of similarity between two parents as a crossover point. Then proceeds to replace the portion selected. 
"""


def homologousonePointcrossover(eaObj, inParent):
    similarpoints = []  # Creating a list to store points with similar angles found
    randParent = Pose()

    # Searching for similar angles
    while (len(similarpoints) == 0):
        randParent.assign(randomParent(eaObj, inParent))
        for i in range(1, inParent.pose.size()):
            if((inParent.pose.phi(i) == randParent.phi(i)) and
                (inParent.pose.psi(i) == randParent.psi(i)) and
                    (inParent.pose.omega(i) == randParent.omega(i))):
                similarpoints.append(i)

    child = Pose()
    child.assign(inParent.pose)

    # Now we select a random point from the list of points that had similar angles as our crossOverPoint
    crossOverPoint = random.choice(similarpoints)

    # We should switch the values from the parents
    for residue in range(1, crossOverPoint):
        Pose.replace_residue(
            child, residue, Pose.residue(randParent, residue), True)

    inParent.pose.assign(child)
