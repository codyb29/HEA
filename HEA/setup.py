import setup_modules as setup


def run(eaObj, cfg):
    # Create ability to read ini files. More specifically, the config section in this particular case.
    setup.config(eaObj, cfg)
    # Object references created:
    # eaObj.cfg

    # Extrapolate information within the ini file. "bh" is concerned more with fasta files.
    initConfig = eaObj.cfg['init']
    setup.bh(eaObj, initConfig)
    # Object references created:
    # eaObj.genN, eaObj.pdbid, eaObj.proteinPath, eaObj.sequence, eaObj.initialPose, eaObj.seqlen

    # Convert the Protein of interest into an easier form of analysis.
    setup.converter(eaObj)
    # Object references created:
    # eaObj.fa2cen, eaObj.cen2fa

    # setting up the variation function
    varConfig = eaObj.cfg['variation']
    setup.variation(eaObj, varConfig)
    # Object references created:
    # eaObj.varFragLength, eaObj.varFragments, eaObj.movemap, eaObj.varMover

    # Generate population based on specified parameters
    setup.GeneratePopulation(eaObj, initConfig)
    # Object references created:
    # eaObj.population

    # TODO: Something needs to be done here.
    setup.evaluation(eaObj, initConfig)
    # Object references created:
    # eaObj.evalnum, eaObj.evalbudget, eaObj.knownNative, eaObj.other

    # Setting up the environment for local search
    impConfig = eaObj.cfg['improvement']
    setup.improvement(eaObj, impConfig)
    # Object references created:
    # eaObj.relaxtype, eaObj.impScoreFxn

    # misc variables
    setup.misc(eaObj)
    # Object references created:
    # eaObj.oSet, eaObj.minScore, eaObj.minState
