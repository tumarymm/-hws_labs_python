def deep_sum(a):
    b = 0
    for c in a.values():
        if isinstance(c, int):
            b += c
        elif isinstance(c, list):
            b += sum(c)
        elif isinstance(c, dict):
            b += deep_sum(c)
    return b