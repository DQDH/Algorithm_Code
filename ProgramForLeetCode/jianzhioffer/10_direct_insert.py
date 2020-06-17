def direct_insert(nums):
    res=[nums[0]]
    for i in range(1,len(nums)):
        if nums[i]>=res[-1]:
            res.append(nums[i])
            continue
        else:
            for j in range(i):
                if nums[i]<res[j]:
                    res=res[:j]+[nums[i]]+res[j:]
                    break
    return res
print(direct_insert([4,1,3,2,5,3,7,3,5,8,2,4,9,2,62,8]))