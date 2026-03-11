def filter_sets(a):
    b = []
    for c in a:
        if len(c) > 3 and all(d >= 0 for d in c) and any(d % 2 == 0 for d in c):
            b.append(c)
    return b