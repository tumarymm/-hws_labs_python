
def replace_every_nth(t, n, c):
    result = ""
    for i, ch in enumerate(t):
        if (i + 1) % n == 0 and not ch.isdigit() and ch != " " and len(t) >= 3:
            result += c
        else:
            result += ch
    return result

if __name__ == "__main__":
    print(replace_every_nth("abcdefg123", 3, "X"))