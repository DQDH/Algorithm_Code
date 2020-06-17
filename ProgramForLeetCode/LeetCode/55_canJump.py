class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res=True
        for i in range(len(nums)):
            if nums[i]==0:
                res=False
                for j in range(i):
                    if nums[j]+j>i:
                        res=True
                        break
            if not res:
                return res
        return res
    def canJump1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def helper(idx):
            if idx == 0:
                return True
            for i in range(idx):
                if nums[i] >= idx - i:
                    if helper(i):
                        return True
            return False

        return helper(len(nums) - 1)
print(Solution().canJump([2,0,1,0,1]))