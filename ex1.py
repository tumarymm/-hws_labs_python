def analyze_text(a):

    b = "aeiou"
    c = a.lower()

    d = ""
    for e in c:
        if e.isalpha() or e == " ":
            d += e
        else:
            d += " "

    f = []
    for e in d:
        if e in b and e not in f:
            f.append(e)

    g = d.split()

    h = []
    for i in g:
        if len(i) >= 5:
            if i[0] == i[-1]:
                if i not in h:
                    h.append(i)

    return (len(f), " ".join(h))