class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        used=[]
        while True:
            str_n = str(n)
            r = sum([int(k)**2 for k in list(str_n)])
            if r==1:
                return True
            elif r in used:
                return False
            else:
                used.append(r)
                n=r
print(Solution().isHappy(7))