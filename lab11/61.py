r = lambda a: {b: c for b, c in a.items() if all(len(d) > 3 for d in c) and len(set(c)) == len(c)}
