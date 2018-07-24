from pyrosetta import create_score_function


def improvement(eaObj, impcfg):
    eaObj.relaxtype = impcfg['relaxtype']  # For now, should be 'local' for HEA
    eaObj.impScoreFxn = create_score_function(
        impcfg['scorefxn'])  # Identify the scoring protocol
