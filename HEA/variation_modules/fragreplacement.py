
def fragReplace(eaObj, pose):
    eaObj.varMover.apply(pose)
    return eaObj.impScoreFxn(pose)
