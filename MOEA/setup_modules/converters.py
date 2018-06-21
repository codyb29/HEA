from pyrosetta import *
from rosetta import *

# TODO: What is this file meant for?
# Centroid representation: Cuts all the side chains
def converter(eaObj):
    eaObj.fa2cen = SwitchResidueTypeSetMover("centroid")
    eaObj.cen2fa = protocols.simple_moves.ReturnSidechainMover(
        eaObj.initialPose)
