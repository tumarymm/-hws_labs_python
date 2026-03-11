def common_elements_all(a):
    if not a:
        return set()
    b = a[0].copy()
    for c in a[1:]:
        b &= c
    return b