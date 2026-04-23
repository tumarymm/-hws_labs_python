def top_k_smallest_unique(a, k):
    b = sorted(set(a))
    return set(b[:k])