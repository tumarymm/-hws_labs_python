def remove_duplicates_keep_last(nums):
    seen={}
    for i,n in enumerate(nums):
        seen[n]=i
    return [nums[i] for i in sorted(seen.values())]