def longest_increasing_sublist(nums):
    res=[]
    temp=[]
    for n in nums:
        if not temp or n>temp[-1]:
            temp.append(n)
        else:
            if len(temp)>len(res):
                res=temp
            temp=[n]
    if len(temp)>len(res):
        res=temp
    return res