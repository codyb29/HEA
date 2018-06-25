from pyrosetta import *
from rosetta import *

# Centroid representation: Cuts all the side chains. Will make the analysis of
# the protein easier.
def converter(eaObj):
    eaObj.fa2cen = SwitchResidueTypeSetMover("centroid")
    eaObj.cen2fa = protocols.simple_moves.ReturnSidechainMover(
        eaObj.initialPose)
