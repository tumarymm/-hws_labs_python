def moving_average(nums,k):
    res=[]
    for i in range(len(nums)-k+1):
        w=nums[i:i+k]
        if any(x<0 for x in w):
            continue
        res.append(sum(w)/k)
    return res