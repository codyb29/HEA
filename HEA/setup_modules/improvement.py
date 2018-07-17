from pyrosetta import *
from rosetta import *
from .utils import getTrueValues


def improvement(eaObj, impcfg):
    eaObj.relaxtype = impcfg['relaxtype']  # For now, should be 'local' for HEA
    eaObj.impScoreFxn = create_score_function(
        impcfg['scorefxn'])  # Identify the scoring protocol
    print ("WHAALJF:LSKDJF:LSDKJF:SLDKJF:SDLKFJ:SLDKFJS:LDKFJ")
