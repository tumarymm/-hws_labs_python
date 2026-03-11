def all_subsets_of_size_k(a, k):
    from itertools import combinations
    return [set(c) for c in combinations(a, k)]