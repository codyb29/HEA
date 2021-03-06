from core import Pose


def local(eaObj, childData):
    # Initial score of the incoming protein conformation
    curScore = childData.score
    discardnum = 0  # Number of failures to improve the score
    tempPose = Pose()

    while discardnum < eaObj.seqLen:
        # Create a duplicate protein that's subject to change
        tempPose.assign(childData.pose)
        eaObj.varMover.apply(tempPose)  # Molecular Fragment Replacement
        # Rescore the adjusted protein conformation
        tempScore = eaObj.impScoreFxn(tempPose)
        eaObj.evalnum += 1

        if tempScore < curScore:
            # When the score is improved, update the current score
            curScore = tempScore
            # Set our improved protein conformation as our new subject
            childData.pose.assign(tempPose)
            discardnum = 0 # reset since we're only concerned with consecutive	
        else:
            # Otherwise, we have failed to improve the score
            discardnum += 1
    
    childData.score = curScore
