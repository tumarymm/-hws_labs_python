def flatten_and_filter(lst):
    res=[]
    def helper(l):
        for x in l:
            if type(x)==list:
                helper(x)
            elif x>0 and x%4!=0 and x>9:
                res.append(x)
    helper(lst)
    return sorted(res)