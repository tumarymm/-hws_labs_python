s = lambda a: {b: c for b, c in a.items() if sum(c)/len(c) > sum(sum(d) for d in a.values())/sum(len(d) for d in a.values())}
