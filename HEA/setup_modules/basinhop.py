from .utils import seq_from_fasta
from pyrosetta import pose_from_sequence, pose_from_pdb


def bh(eaObj, initcfg):
    # Create references to variables in ini file
    eaObj.genN = int(initcfg['nGen'])
    eaObj.pdbid = initcfg['protein']
    eaObj.proteinPath = initcfg['path']

    # 3 different initialization states
    # The protein can be instantiated through 3 different file types:
    # .fasta, .pdb, or a sequence file.
    if initcfg['initState'] == 'extended':
        eaObj.sequence = seq_from_fasta(
            eaObj.proteinPath + "{0}/{0}.fasta".format(eaObj.pdbid))
        eaObj.initialPose = pose_from_sequence(eaObj.sequence)
    elif initcfg['initState'] == 'pdb':
        eaObj.initialPose = pose_from_pdb(eaObj.proteinPath + "{0}/{0}.pdb".format(eaObj.pdbid))
    elif initcfg['initState'] == 'sequence':
        eaObj.sequence = initcfg['sequence']
        eaObj.initialPose = pose_from_sequence(eaObj.sequence)
    else:
        raise Exception("Unrecognized initState!")

    eaObj.seqlen = len(eaObj.initialPose.sequence())
