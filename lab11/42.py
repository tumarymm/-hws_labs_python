j = lambda a: {b for b in a if b.isalpha() and len(b) > 4 and len(set(b)) == len(b)}
