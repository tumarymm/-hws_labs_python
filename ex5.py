def compress_text(a):

    b = ""
    c = 0

    while c < len(a):

        d = 1

        while c + 1 < len(a) and a[c].lower() == a[c+1].lower():
            d += 1
            c += 1

        if d == 1:
            b += a[c]
        else:
            b += a[c] + str(d)

        c += 1

    return b