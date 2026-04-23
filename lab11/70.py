def analyze_dict_keys(a):
    b = set()
    for c in a:
        if c.isalpha():
            for d in c:
                if d.isalpha():
                    b.add(d)
    return b