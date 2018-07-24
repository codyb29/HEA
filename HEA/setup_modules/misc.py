from core import Pose


def misc(eaObj):
    # offspring set
    eaObj.oSet = set()
    # mintracker
    eaObj.minScore = 1e9
    eaObj.minState = Pose()
