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
    # TODO: Make the "3"s more modular
    fragData = core.fragment.ConstantLengthFragSet(3)
    fragData.read_fragment_file(
        eaObj.proteinPath + "{0}/aat000_0{1}_05.200_v1_3".format(eaObj.pdbid, 3))

    # Create the initial population specified in the ini file
    size = 0
    maxPopulation = int(initcfg['population'])
    while (size < maxPopulation):
        # new protein to be added to population that is subject to a randomized conformation
        newPose = Pose()
        newPose.assign(eaObj.initialPose) 
        eaObj.fa2cen.apply(newPose) # Will convert the protein into a centroid.

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