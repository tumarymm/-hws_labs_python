a = lambda b: sum(
    1
    for c in b.split()
    if any(d.isdigit() for d in c) and not c[0].isdigit() and len(c) >= 5
)