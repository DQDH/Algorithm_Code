class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            for element in nums:
                if element==val:
                    nums.remove(element)
        return len(nums)
    def removeElement2(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)

nums = [0,1,2,2,3,0,4,2]
val = 2
a=Solution().removeElement(nums,val)