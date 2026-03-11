def merge_dicts_sum(a, b):
    c = a.copy()
    for d, e in b.items():
        c[d] = c.get(d, 0) + e
    return c