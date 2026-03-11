def multi_symmetric_difference(a):
    b = set()
    for c in a:
        b ^= c
    return b