def top_k_frequent(a, k):
    b = {}
    for c in a:
        b[c] = b.get(c, 0) + 1
    d = sorted(b.items(), key=lambda x: (-x[1], x[0]))
    e = [x[0] for x in d][:k]
    return set(e)