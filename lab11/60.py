def partition_by_sum_parity(a):
    b = set()
    c = set()
    for d in a:
        if sum(int(e) for e in str(abs(d))) % 2 == 0:
            b.add(d)
        else:
            c.add(d)
    return (b, c)