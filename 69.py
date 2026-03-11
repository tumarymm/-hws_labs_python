v = lambda a: sorted(a, key=lambda b: (sum(1 for c in b if c in 'aeiouAEIOU'), -a[b]))
