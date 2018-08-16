from rosetta import core, protocols
from pyrosetta import MoveMap

"""
Setting up the Molecular Fragment Replacement.
"""


def variation(eaObj, varcfg):
    # setting the constant length of fragments being replaced
    eaObj.varFragLength = int(varcfg['fragLength'])
    # uses our previously defined value to set the fragment length of the fragment set in pyrosetta using data
    eaObj.varFragments = core.fragment.ConstantLengthFragSet(
        eaObj.varFragLength)
    # reads our fragment file from the path generated using our previously defined values for the protein's id and the length specified for each fragment (3 or 9)
    eaObj.varFragments.read_fragment_file(
        eaObj.proteinPath + "{0}/aat000_0{1}_05.200_v1_3".format(eaObj.pdbid, eaObj.varFragLength))
    eaObj.movemap = MoveMap()  # Enables movement of the abstract Pose object.
    # Allows all backbone torsion angles to vary
    eaObj.movemap.set_bb(int(varcfg['bbAngle']) == 1)
    # Allows all side-chain torsion angles (χ) to vary
    eaObj.movemap.set_chi(int(varcfg['chiAngle']) == 1)
    eaObj.varMover = protocols.simple_moves.ClassicFragmentMover(
        eaObj.varFragments, eaObj.movemap)  # Using the fragments extracted, it will move a Pose according to the allowed movement from MoveMap()
