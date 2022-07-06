def subsets(elements, power_set=[[]], ind=0):
    if len(elements) == ind:
        return power_set

    for set in power_set.copy():
        set_include = set.copy()
        set_include.append(elements[ind])
        power_set.append(set_include)

    return subsets(elements, power_set, ind+1)
