n = lambda a, b: {x for x in a if x > sum(b)/len(b) and x not in b}
