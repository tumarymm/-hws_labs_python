def union_of_filtered_sets(a):
    b = set()
    for c in a:
        b |= {d for d in c if d > 10 and d % 2 == 1}
    return b