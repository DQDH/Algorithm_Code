class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=0
        r=[]
        for i in range(len(digits)):
            s=s+digits[i]*10**(len(digits)-i-1)
        s=s+1
        while s!=0:
            r.append(s%10)
            s=s//10
        return r.reverse()
Solution().plusOne([1,2,3])