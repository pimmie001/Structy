def intersection(a, b):
    a = set(a)
    b = set(b)
    intersect = []
    
    for x in a:
        if x in b:
            intersect.append(x)

    return intersect
