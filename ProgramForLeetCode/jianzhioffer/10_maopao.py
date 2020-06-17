def maopao(nums):
    i=0
    while i<len(nums):
        for j in range(len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
        i+=1
    return nums
print(maopao([2,1,5,3,8,9,1,3,4]))