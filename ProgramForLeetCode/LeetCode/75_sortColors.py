class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left,current,right=0,0,len(nums)-1
        while current<=right:
            if left>right:
                break
            if nums[current]==0:
                nums[left],nums[current]=nums[current],nums[left]
                left+=1
                current+=1
            elif nums[current]==2:
                nums[right],nums[current]=nums[current],nums[right]
                right-=1
            else:
                current+=1
        return nums
    def sortColors1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count=[0,0,0]
        for nums_i in nums:
            if nums_i==0:
                count[0]+=1
            elif nums_i==1:
                count[1]+=1
            else:
                count[2]+=1
        i=0
        while count[0]>0:
            nums[i]=0
            i+=1
            count[0]-=1
        while count[1]>0:
            nums[i] = 1
            i += 1
            count[1] -= 1
        while count[2]>0:
            nums[i] = 2
            i += 1
            count[2] -= 1
        return nums
print(Solution().sortColors([2,0,1]))