def palindrome_words(a):

    b = ""

    for c in a.lower():
        if c.isalpha() or c == " ":
            b += c
        else:
            b += " "

    d = b.split()

    e = []

    for f in d:
        if len(f) >= 3:
            if f == f[::-1]:
                if f not in e:
                    e.append(f)

    e.sort(key=lambda g: (-len(g), g))

    return e