def sort_dict_by_value_length(a):
    return sorted(a.items(), key=lambda b: (len(b[1]), b[0]))