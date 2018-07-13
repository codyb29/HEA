from core import Pose


def local(eaObj, pose):
    # Initial score of the incoming protein conformation
    curScore = eaObj.impScoreFxn(pose)
    eaObj.evalnum += 1  # The amount of times a protein has been evaluated.
    discardnum = 0  # Number of failures to improve the score
    tempPose = Pose()

    while discardnum < eaObj.seqlen:
        # Create a duplicate protein that's subject to change
        tempPose.assign(pose)
        eaObj.varMover.apply(tempPose)  # Molecular Fragment Replacement
        # Rescore the adjusted protein conformation
        tempScore = eaObj.impScoreFxn(tempPose)
        eaObj.evalnum += 1

        if tempScore < curScore:
            # When the score is improved, update the current score
            curScore = tempScore
            # Set our improved protein conformation as our new subject
            pose.assign(tempPose)
        else:
            # Otherwise, we have failed to improve the score
            discardnum += 1

    return curScore
