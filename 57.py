p = lambda a: {b: c for b, c in a.items() if c > 1 and all(c % i != 0 for i in range(2, int(c**0.5)+1)) and len(b) % 2 == 1}
