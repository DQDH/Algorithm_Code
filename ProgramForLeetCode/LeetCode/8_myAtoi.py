class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res=0
        str=str.lstrip(' ')
        signal=['+','-']
        if len(str)==0 or str in signal:
            return res
        if str[0] not in signal:
            ascii_s = ord(str[0])
        else:
            ascii_s = ord(str[1])
        if ascii_s>57 or ascii_s<48:
            return res

        str=str.split(' ')
        f=2 ** 31
        index=len(str[0])
        for i in range(1,len(str[0])):
            if (str[0][i]<'0'or str[0][i]>'9'):
                index=i
                break
        if str[0][0]=='-':
            res = -int(str[0][1:index])
            if res< -f:
                return -f
        else:
            res=int(str[0][:index])
            if res>f-1:
                return f-1
        return res
Solution().myAtoi("+1")