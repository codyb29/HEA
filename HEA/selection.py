import selection_modules as selection


def select(eaObj):
    return selection.hea(eaObj)


def truncate(eaObj, poses, tposes):
    return selection.truncate(eaObj, poses, tposes)
