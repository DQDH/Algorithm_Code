class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=bin(n).count('1')
        return res
Solution().hammingWeight(1011)