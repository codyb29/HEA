import selection_modules as selection


def select(eaObj):
    """
    Not needed for HEA purposes
    selectionType = eaObj.cfg['selection']['type']
    if selectionType == 'opo':
        return selection.oneplusone(eaObj)
    if selectionType == 'moea':
        return selection.moea(eaObj)
    """
    return selection.hea(eaObj)


def truncate(eaObj, poses, tposes):
    return selection.truncate(eaObj, poses, tposes)
