o = lambda a: {b: (lambda x=1: [x := x * d for d in c][ -1] if c else 1)() for b, c in a.items() if c}
