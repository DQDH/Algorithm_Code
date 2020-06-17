class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        if n%2==0 and n!=0:
            return self.isPowerOfTwo(n//2)
        else:
            return False
print(Solution().isPowerOfTwo(0))