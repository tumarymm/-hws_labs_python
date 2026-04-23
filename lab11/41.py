def group_by_length(a):
    b = {}
    for c in a:
        d = len(c)
        if d not in b:
            b[d] = [c]
        else:
            if c not in b[d]:
                b[d].append(c)
    return b