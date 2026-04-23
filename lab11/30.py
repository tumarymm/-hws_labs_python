def analyze_strings_list(l):
    res=[]
    for w in l:
        if len(w)>3 and w[0].isupper() and w[-1].islower():
            res.append(w[::-1])
    return res