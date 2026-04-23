

task12 = lambda t: [w for w in t.split() if len(w) > 3 and w[0].lower() == w[-1].lower() and w.lower() != w.lower()[::-1]]

if __name__ == "__main__":
    print(task12("level noon civic radar refer rotor kayak madam"))