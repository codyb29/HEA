from core import Pose


def local(eaObj, posePair):
    # TODO: This can be improved. Data is already scored and stored. Just need to import array somehow.
    # Initial score of the incoming protein conformation
    curScore = posePair[1]
    discardnum = 0  # Number of failures to improve the score
    tempPose = Pose()

    while discardnum < eaObj.seqlen:
        # Create a duplicate protein that's subject to change
        tempPose.assign(posePair[0])
        eaObj.varMover.apply(tempPose)  # Molecular Fragment Replacement
        # Rescore the adjusted protein conformation
        tempScore = eaObj.impScoreFxn(tempPose)
        eaObj.evalnum += 1

        if tempScore < curScore:
            # When the score is improved, update the current score
            curScore = tempScore
            # Set our improved protein conformation as our new subject
            posePair[0].assign(tempPose)
        else:
            # Otherwise, we have failed to improve the score
            discardnum += 1

    return curScore
