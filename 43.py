def invert_dict_strict(a):
    b = {}
    c = {}
    for d, e in a.items():
        if e not in c:
            c[e] = 1
        else:
            c[e] += 1
    for d, e in a.items():
        if c[e] == 1:
            b[e] = d
    return b
