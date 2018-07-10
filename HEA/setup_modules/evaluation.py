from pyrosetta import *
from rosetta import *

def evaluation(eaObj, initcfg):
    eaObj.evalnum = 0 # How many runs we are currently at.
    eaObj.evalbudget = int(initcfg['evalbudget']) # How many runs we can afford to do.
    # Based off the given native structure, we score our algorithm's prediction
    eaObj.knownNative = pose_from_pdb(eaObj.proteinPath + "{0}/{0}.pdb".format(eaObj.pdbid))

    eaObj.other = create_score_function("score3")