k = lambda a: {b: c for b, c in a.items() if c >= sum(a.values())/len(a) and c % 2 == 1}
