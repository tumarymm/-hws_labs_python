def count_leaf_values(a):
    b = 0
    for c in a.values():
        if isinstance(c, dict):
            b += count_leaf_values(c)
        elif isinstance(c, list):
            b += len(c)
        else:
            b += 1
    return b
