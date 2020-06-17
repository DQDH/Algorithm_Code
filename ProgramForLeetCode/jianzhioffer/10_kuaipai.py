def Partition(nums, left, right):
    save = nums[left]
    while left < right:
        while left < right and nums[right] >= save:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= save:
            left += 1
        nums[right] = nums[left]
        nums[left] = save
    return left
def quick_sort(nums,left,right):
    if left<right:
        i=Partition(nums,left,right)
        quick_sort(nums,left,i-1)
        quick_sort(nums,i+1,right)
    return nums
s=[6, 8, 1, 4, 3, 9, 5, 4, 11, 2, 2, 15, 6]
print(quick_sort(s,0,len(s)-1))

'''
def quick_sort(data):    
    """快速排序"""    
    if len(data) >= 2:  # 递归入口及出口        
        mid = data[len(data)//2]  # 选取基准值，也可以选取第一个或最后一个元素        
        left, right = [], []  # 定义基准值左右两侧的列表        
        data.remove(mid)  # 从原始数组中移除基准值        
        for num in data:            
            if num >= mid:                
                right.append(num)            
            else:                
                left.append(num)        
        return quick_sort(left) + [mid] + quick_sort(right)    
    else:        
        return data
 
# 示例：
array = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
print(quick_sort(array))
'''