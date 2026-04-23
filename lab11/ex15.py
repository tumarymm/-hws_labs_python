# ex15.py

def word_pattern_sort(t):
    words = t.split()
    grouped = {}
    vowels = "aeiouAEIOU"
    for w in words:
        l = len(w)
        v_count = sum(1 for ch in w if ch in vowels)
        if l not in grouped:
            grouped[l] = []
        grouped[l].append((w, v_count))
    result = []
    for l in sorted(grouped.keys()):
        sorted_group = sorted(grouped[l], key=lambda x: (-x[1], x[0]))
        result.extend([x[0] for x in sorted_group])
    return result

if __name__ == "__main__":
    print(word_pattern_sort("apple banana kiwi orange pear"))