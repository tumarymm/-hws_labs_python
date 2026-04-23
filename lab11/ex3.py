def top_k_words(a, b):

    c = a.lower()

    d = ""
    for e in c:
        if e.isalpha() or e == " ":
            d += e
        else:
            d += " "

    f = d.split()

    g = {}

    for h in f:
        if h in g:
            g[h] += 1
        else:
            g[h] = 1

    i = list(g.items())

    i.sort(key=lambda j: (-j[1], j[0]))

    k = []
    for l in range(min(b, len(i))):
        k.append(i[l][0])

    return k