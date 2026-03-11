t = lambda a: {b: c for b, c in a.items() if c % 3 != 0 and len(b) % 2 == 1}
