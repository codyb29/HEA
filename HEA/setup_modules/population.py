from pyrosetta import *
from rosetta import *
from math import fabs, sqrt, exp
from random import randint, random


# Implements the Molecular Fragment Replacement as specified in section 2.4 in the paper
def MolFragReplacement(initPose, data):
    #  Allows for the specification for which degrees of freedom are allowed to change in the pose
    movemap = MoveMap()
    movemap.set_bb(True)  # Allows all backbone torsion angles to vary
    # will select a random 3-mer window and insert only the backbone torsion angles from a random matching fragment in the fragment set
    mover_3mer = protocols.simple_moves.ClassicFragmentMover(data, movemap)
    mover_3mer.apply(initPose)

# Will be used to generate the initial randomized population
def GeneratePopulation(eaObj, initcfg):
    eaObj.population = []
    eaObj.randomSeed = False
    # Configurations to use for replacements
    fragData = core.fragment.ConstantLengthFragSet(3)
    fragData.read_fragment_file(
        eaObj.proteinPath + "{0}/aat000_0{1}_05.200_v1_3".format(eaObj.pdbid, 3))

    if initcfg['randomseed'] == '1':
        eaObj.randomSeed = True

    # Create the initial population specified in the ini file
    size = 0
    maxPopulation = int(initcfg['population'])
    while (size < maxPopulation):
        # new protein to be added to population that is subject to a randomized conformation
        newPose = Pose()
        newPose.assign(eaObj.initialPose)

        # Verify successful conversion of centroid representation
        if eaObj.cfg['improvement']['representation'] == 'centroid':
            # Sends the pose coordinates to PyMOL for viewing
            eaObj.fa2cen.apply(newPose)

        # TODO: Verify the need for this portion of code.
        #  Randomly assign dihedral angles for each amino acid
        # if eaObj.randomSeed:
        #    randomSeed(eaObj, newPose)

        MolFragReplacement(newPose, fragData)

        # Add the newly modified protein to the total population
        eaObj.population.append(newPose)
        size += 1



# TODO: Figure out the necessity of this portion of the code. Does not appear to reflect the HEA algorithm.
"""
    # Looks like a quick fix. Probably delete this and find a better way of doing this.
    if len(eaObj.population) < 1:
        return

    eaObj.score0 = create_score_function('score0')
    eaObj.score1 = create_score_function('score1')

    setupfrag = core.fragment.ConstantLengthFragSet(3)
    setupfrag.read_fragment_file(
        eaObj.proteinPath + "aat000_0{0}_05.200_v1_3".format(3))

    setupmm = MoveMap()
    setupmm.set_bb(True)  # Allows all backbone torsion angles to vary
    setupmm.set_chi(True)  # Allows all side-chain torsion angles (χ) to vary
    # A FragmentMover that applies uniform sampling of fragments
    eaObj.setupMover = protocols.simple_moves.ClassicFragmentMover(
        setupfrag, setupmm)

    # For each protein within the population, randomly reconfigure its structure.
    for protein in eaObj.population:
        protein.assign(randomizeConformation(eaObj, protein))

def randomizeConformation(eaObj, ipose):
    base = Pose()
    base.assign(ipose)
    for x in range(200):
        tempPose = Pose()
        tempPose.assign(base)
        eaObj.setupMover.apply(tempPose)
        mc(eaObj, tempPose, base, eaObj.score0)
    discardnum = 0
    while discardnum < eaObj.seqlen:
        tempPose = Pose()
        tempPose.assign(base)
        eaObj.setupMover.apply(tempPose)

        if mc(eaObj, tempPose, base, eaObj.score1):
            continue
        else:
            discardnum += 1

    return base

def mc(eaObj, newPose, oldPose, score):
    # Initiate variables
    diff = score(newPose) - score(oldPose)
    r = random()

    # Evaluate
    tmp = (eaObj.evalnum * 14) / eaObj.evalbudget
    mc = exp(diff / (-14 - tmp))

    # Verify and return
    if diff < 0 or r < mc:
        oldPose.assign(newPose)
        return True

    return False



def randomSeed(eaObj, ipose):
    rg_fxn = ScoreFunction()
    rg_fxn.set_weight(core.scoring.rg, 1)
    # Will continue to try to improve the protein until we meet the specified criteria
    pose = Pose()
    pose.assign(ipose)  # Copy the incoming pose
    clash = create_score_function('score3')

# While the score of the incoming pose minus the sqrt of the sequence length is greater than
# 60% of the sequence length and the score 3 of the incoming pose is greater than 150, randomizeBB.

    while (fabs(rg_fxn(pose) - sqrt(eaObj.seqlen)) > (sqrt(eaObj.seqlen) * .6)) and (clash(pose) >= 150):
        pose.assign(ipose)
        randomizeBB(eaObj, pose)

    # Assign the incoming pose to the accepted criteria protein generated.
    ipose.assign(pose)


def randomizeBB(eaObj, pose):
    # Sets the φ & ψ angles of the ith residue in the pose to a random degree between -180.0° - 180.0°
    for i in range(1, eaObj.seqlen + 1):
        pose.set_phi(i, randint(-180, 180))
        pose.set_psi(i, randint(-180, 180))
"""
