class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def stradd(str1,str2):
            res=''
            str1=str1.zfill(max(len(str1),len(str2)))
            str2=str2.zfill(max(len(str1), len(str2)))
            up=0
            for i in range(len(str1)-1,-1,-1):
                res_i=str(int(str1[i])+int(str2[i])+up)
                if len(res_i)>1:
                    up=1
                else:
                    up=0
                res=res_i[-1]+res
            return res if not up else "1"+res
        if num1[0]=="0" or num2[0]=="0":
            return "0"
        res='0'
        num1_1=num1.rstrip("0")
        num2_1=num2.rstrip("0")
        end="0"*(len(num1)+len(num2)-len(num1_1)-len(num2_1))
        if len(num1_1)<len(num2_1):
            tmp=num1_1
            num1_1=num2_1
            num2_1=tmp
        for j in range(len(num2_1)-1,-1,-1):
            tmp='0'
            for i in range(1,int(num2_1[j])+1):
                tmp=stradd(tmp,num1_1)
            tmp=tmp+"0"*(len(num2_1)-1-j)
            res=stradd(res,tmp)
        return res+end
print(Solution().multiply("7967","7067"))