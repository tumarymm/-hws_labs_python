def invert_unique(a):
    b = {}
    for c, d in a.items():
        if d not in b:
            b[d] = [c]
        else:
            if c not in b[d]:
                b[d].append(c)
    return b