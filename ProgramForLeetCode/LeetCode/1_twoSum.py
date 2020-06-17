class Solution:
    def twoSum1(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j
    def twoSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            dst=target-nums[i]
            if dst in nums and i!=nums.index(dst):
                return i,nums.index(dst)
solution=Solution()
nums = [2, 11,7, 15]
target = 9
a,b=solution.twoSum1(nums,target)
print(a,b)