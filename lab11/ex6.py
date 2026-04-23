a = lambda b: list(
    filter(
        lambda c: len(c) >= 4 and c.isalpha() and len(set(c)) == len(c),
        b.split()
    )
)