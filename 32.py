f = lambda a: {b for b in a if b > sum(a)/len(a) and b % 2 == 1 and b % 5 != 0}
