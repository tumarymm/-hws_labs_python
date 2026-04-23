def sort_dict_by_value_sum(a):
    b = []
    for c, d in a.items():
        b.append((c, sum(d)))
    b.sort(key=lambda x: (-x[1], x[0]))
    return b