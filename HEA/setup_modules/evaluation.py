from pyrosetta import pose_from_pdb


def evaluation(eaObj, initcfg):
    eaObj.evalnum = 0  # How many runs we are currently at.
    # How many runs we can afford to do.
    eaObj.evalbudget = int(initcfg['evalbudget'])
    # Based off the given native structure, we score our algorithm's prediction
    eaObj.knownNative = pose_from_pdb(
        eaObj.proteinPath + "{0}/{0}.pdb".format(eaObj.pdbid))
    # Initially created for superimposing 2 proteins where they may or may not have the same size sequence length. 
    eaObj.knownNativeLen = eaObj.knownNative.size()
