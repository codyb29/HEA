import setup_modules as setup


def run(eaObj, cfg):
    # Create ability to read ini files. More specifically, the config section in this particular case.
    setup.config(eaObj, cfg)

    # Extrapolate more information within the ini file. "bh" is concerned more with fasta files.
    initConfig = eaObj.cfg['init']
    setup.bh(eaObj, initConfig)
    setup.converter(eaObj) # Convert the Protein of interest into an easier form of analysis.
    setup.GeneratePopulation(eaObj, initConfig) # Generate population based on specified parameters
    setup.evaluation(eaObj, initConfig) # TODO: What the hell is going on here...

    # setting up the variation function
    varConfig = eaObj.cfg['variation'] 
    setup.variation(eaObj, varConfig)

    # setting up the improvement
    impConfig = eaObj.cfg['improvement']
    setup.improvement(eaObj, impConfig)

    # misc variables
    setup.misc(eaObj)
