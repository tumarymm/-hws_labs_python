a = lambda b: " ".join(
    [
        c if any(d.isdigit() for d in c)
        else "VOWEL" if c[0].lower() in "aeiou"
        else "CONSONANT"
        for c in b.split()
    ]
)