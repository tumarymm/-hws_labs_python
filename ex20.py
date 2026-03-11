def max_subarray_sum(nums,k):
    maxs=None
    for i in range(len(nums)-k+1):
        s=nums[i:i+k]
        if any(x<=0 for x in s):
            continue
        t=sum(s)
        if maxs is None or t>maxs:
            maxs=t
    return maxs