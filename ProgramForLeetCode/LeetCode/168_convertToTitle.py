class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result=""
        if n<=26:
            return chr(n+64)
        else:
            num_s=n
            while num_s>26:
                num_g = num_s % 26
                num_s = num_s // 26
                if num_g==0:
                    num_s=num_s-1
                    result="Z"+result
                else:
                    result=chr(num_g+64)+result
            result=chr(num_s+64)+result
            return result
Solution().convertToTitle(53)