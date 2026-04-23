def filter_by_digit_sum(a):
    b = set()
    for c in a:
        if sum(int(d) for d in str(abs(c))) % 2 == 0 and c % 2 == 1:
            b.add(c)
    return b