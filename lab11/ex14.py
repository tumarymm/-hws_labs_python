
task14 = lambda t: ",".join([w for w in t.split() if len(set(w)) > 3 and all(w.count(v) == 1 for v in "aeiouAEIOU" if v in w)])

if __name__ == "__main__":
    print(task14("apple orange banana kiwi"))