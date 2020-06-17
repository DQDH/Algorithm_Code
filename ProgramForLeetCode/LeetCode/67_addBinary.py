class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a)-len(b)>0:
            bb=b.zfill(len(a))
            aa=a
        else:
            aa=a.zfill(len(b))
            bb=b
        l=0
        r=''
        for i in range(len(aa)-1,-1,-1):
            c=int(aa[i])+int(bb[i])+l
            if c==0 or c==1:
                l=0
                r=str(c)+r
            if c==2:
                l=1
                r='0'+r
            if c==3:
                l=1
                r='1'+r
        if l==1:
            r='1'+r
        return r

a='11111'
b='1111'
print(Solution().addBinary(a,b))