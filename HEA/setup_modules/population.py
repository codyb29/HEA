from rosetta.protocols.grafting import delete_region
from rosetta.core.pose import compare_atom_coordinates
from math import inf
from copy import deepcopy
import setup_modules as setup
from pyrosetta import Pose

# Wrapper class to intuitively store relevant data pertaining to a given protein conformation.
class ProteinData :
    def __init__(self, pose, score):
        self.pose = pose
        self.score = score
        self.age = 0 # Initially 0, as it has not progressed a generation yet.
        self.rmsd = inf # rmsd is not required initially
    
    # Allows for easy comparison between two protein conformation.
    def __eq__( self, other) :
        return compare_atom_coordinates(self.pose, other.pose)


# Will be used to generate the initial randomized population
def GeneratePopulation(eaObj, initcfg):
    eaObj.population = []

    # Truncation starting point
    delStart = min(eaObj.seqLen, eaObj.knownNativeLen)
    delEnd = max(eaObj.seqLen, eaObj.knownNativeLen)  # Truncation ending point
    if (((delEnd - delStart) >= 1) and (eaObj.knownNativeLen == delEnd)):
        delete_region(eaObj.knownNative, delStart + 1, delEnd)

    # Create the initial population specified in the ini file
    size = 0
    maxPopulation = int(initcfg['population'])
    while (size < maxPopulation):
        # new protein to be added to population that is subject to a randomized conformation
        newPose = Pose()
        newPose.assign(eaObj.initialPose)
        # Will convert the protein into a centroid.
        eaObj.fa2cen.apply(newPose)
        eaObj.varMover.apply(newPose)  # Molecular fragment replacement
        if (((delEnd - delStart) >= 1) and (eaObj.seqLen == delEnd)):
            delete_region(newPose, delStart + 1, delEnd)
        # Add the newly modified protein to the total population
        eaObj.population.append(ProteinData(newPose, eaObj.impScoreFxn(newPose)))
        eaObj.evalnum += 1
        size += 1
