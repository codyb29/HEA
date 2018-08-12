from rosetta.protocols.grafting import delete_region
import setup_modules as setup
from core import Pose


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
        eaObj.population.append([newPose, eaObj.impScoreFxn(newPose)])
        eaObj.evalnum += 1
        size += 1
