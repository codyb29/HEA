from .utils import seq_from_fasta
from pyrosetta import *
from rosetta import *


def bh(eaObj, initcfg):
    # Create references to variables in ini file
    eaObj.genN = int(initcfg['nGen'])
    eaObj.pdbid = initcfg['protein']
    eaObj.proteinPath = initcfg['path']

    # 3 different initialization states
    # TODO: VERIFY THESE ARE CORRECT
    if initcfg['initState'] == 'extended':
        eaObj.sequence = seq_from_fasta(
            eaObj.proteinPath + "{0}.fasta".format(eaObj.pdbid))
        eaObj.initialPose = pose_from_sequence(eaObj.sequence)
    elif initcfg['initState'] == 'pdb':
        eaObj.initialPose = pose_from_pdb(eaObj.proteinPath + "{0}/{0}.pdb")
    elif initcfg['initState'] == 'sequence':
        eaObj.sequence = initcfg['sequence']
        eaObj.initialPose = pose_from_sequence(eaObj.sequence)
    else:
        raise Exception("Unrecognized initState!")

    eaObj.seqlen = len(eaObj.initialPose.sequence())
