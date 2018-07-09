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
    # eaObj.genN, eaObj.pdbid, eaObj.proteinPath, eaObj.sequence, eaObj.initialPose

    # Convert the Protein of interest into an easier form of analysis.
    setup.converter(eaObj)
    # Object references created:
    # eaObj.fa2cen, eaObj.cen2fa

    # Generate population based on specified parameters
    setup.GeneratePopulation(eaObj, initConfig)
    # TODO: What the hell is going on here...
    setup.evaluation(eaObj, initConfig)

    # setting up the variation function
    varConfig = eaObj.cfg['variation']
    setup.variation(eaObj, varConfig)

    # setting up the improvement
    impConfig = eaObj.cfg['improvement']
    setup.improvement(eaObj, impConfig)

    # misc variables
    setup.misc(eaObj)
