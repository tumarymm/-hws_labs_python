

def common_unique_chars(a, b):
    result = ""
    for c in a:
        if c in b and c.isalpha() and c not in result:
            result += c
    return result

if __name__ == "__main__":
    print(common_unique_chars("hello world", "hold"))