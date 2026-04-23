def remove_elements_with_common_digits(a):
    b = {}
    for c in a:
        for d in str(abs(c)):
            if d not in b:
                b[d] = 1
            else:
                b[d] += 1
    return {c for c in a if all(b[d] == 1 for d in str(abs(c)))}