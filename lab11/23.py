def group_by_parity_and_sort(nums):
    e=sorted([x for x in nums if x%2==0])
    o=sorted([x for x in nums if x%2==1])
    return e+o