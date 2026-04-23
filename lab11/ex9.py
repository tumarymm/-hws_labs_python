def alternate_case_blocks(a, b):

    c = ""
    d = 0
    e = 0

    while d < len(a):

        f = a[d:d+b]

        if e % 2 == 0:
            c += f.upper()
        else:
            c += f.lower()

        d += b
        e += 1

    return c