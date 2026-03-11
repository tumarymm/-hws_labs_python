def group_by_last_letter(a):
    b = {}
    for c in a:
        d = c[-1]
        if d not in b:
            b[d] = [c]
        else:
            if c not in b[d]:
                b[d].append(c)
    return b