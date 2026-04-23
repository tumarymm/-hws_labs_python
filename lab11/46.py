def update_counts(a, b):
    for c in b:
        if c in a:
            a[c] += 1
        else:
            a[c] = 1
    return a