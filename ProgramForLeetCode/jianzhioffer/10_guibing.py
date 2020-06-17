def merge(l, r):
    i, j = 0, 0
    res = []
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    while i < len(l):
        res.append(l[i])
        i += 1
    while j < len(r):
        res.append(r[j])
        j += 1
    return res
def merge_sort(nums):
    if len(nums)<=1:
        return nums
    m=len(nums)//2
    left=merge_sort(nums[:m])
    right=merge_sort(nums[m:])
    res=merge(left,right)
    return res
print(merge_sort([1,4,8,2,5,4,6]))