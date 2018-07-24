from pyrosetta import SwitchResidueTypeSetMover
from rosetta.protocols import simple_moves

# Gives object attributes to convert from Centroid representation and full representation


def converter(eaObj):
    # low-resolution representation, will make calculations much quicker.
    eaObj.fa2cen = SwitchResidueTypeSetMover("centroid")
    eaObj.cen2fa = simple_moves.ReturnSidechainMover(
        eaObj.initialPose)  # Switch back
