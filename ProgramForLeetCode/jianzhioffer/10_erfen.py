def dichotomy(nums,k):
    l,r=0,len(nums)
    m=len(nums)//2
    while l<r:
        if nums[m]==k:
            return m
        if nums[l]<k<nums[m]:
            r=m
            m=(l+r)//2
        else:
            l=m
            m = (l + r) // 2
print(dichotomy([1,2,4,5,6,8],4))