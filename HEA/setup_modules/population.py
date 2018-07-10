from pyrosetta import *
from rosetta import *
import setup_modules as setup
from math import fabs, sqrt, exp
from random import randint, random


# Will be used to generate the initial randomized population
def GeneratePopulation(eaObj, initcfg):
    eaObj.population = []

    # Create the initial population specified in the ini file
    size = 0
    maxPopulation = int(initcfg['population'])
    while (size < maxPopulation):
        # new protein to be added to population that is subject to a randomized conformation
        newPose = Pose()
        newPose.assign(eaObj.initialPose) 
        eaObj.fa2cen.apply(newPose) # Will convert the protein into a centroid.
        for i in range(0, eaObj.seqlen) :
            eaObj.varMover.apply(newPose) # Molecular fragment replacement
        # Add the newly modified protein to the total population
        eaObj.population.append(newPose)
        size += 1