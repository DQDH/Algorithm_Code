class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict={}
        for nums_i in nums:
            if nums_i not in dict:
                dict[nums_i]=1
            else:
                return True
        return False
print(Solution().containsDuplicate([1,2,3]))