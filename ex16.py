def transform_list(nums):
    res=[]
    for n in nums:
        if n<0:
            continue
        if n%2==0:
            res.append(n**2)
        elif n>10:
            res.append(sum(int(d) for d in str(n)))
        else:
            res.append(n)
    return res