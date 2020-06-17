def direct_chioce(nums):
    for i in range(len(nums)):
        min_num=nums[i]
        min_num_index=i
        for j in range(i+1,len(nums)):
            if nums[j]<min_num:
                min_num=nums[j]
                min_num_index=j
        nums[i],nums[min_num_index]=nums[min_num_index],nums[i]
    return nums
print(direct_chioce([4,1,3,2,5,3,7,3,5,8,2,4,9,2,62,8]))