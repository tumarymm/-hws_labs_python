def sorted_unique_chars(a):
    b = set()
    for c in a:
        for d in c:
            if d.isalpha():
                b.add(d)
    return sorted(b)