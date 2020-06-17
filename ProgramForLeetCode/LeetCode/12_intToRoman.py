# class Solution1(object):
#     def index_n(self,num):
#         n = [1, 5, 10, 50, 100, 500, 1000,5000]
#         s = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
#
#         for ni in n:
#             if num<ni:
#                 return s[n.index(ni)-1],n[n.index(ni)-1]
#
#     def intToRoman(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#         r=''
#         dict1 = {'VIIII': 'IX', 'LXXXX': 'XC', 'DCCCC': 'CM'}
#         dict2 = {'IIII':'IV','XXXX':'XL','CCCC':'CD'}
#         while num!=0:
#             ss,n=Solution().index_n(num)
#             r=r+ss
#             num=num-n
#         for key,value in dict1.items():
#             if key in r:
#                 r=r.replace(key,value)
#         for key, value in dict2.items():
#             if key in r:
#                 r=r.replace(key, value)
#         return r

class Solution(object):
    def index_n(self, num):
        n = [1, 4,5, 9,10,40, 50,90, 100, 400,500,900, 1000, 4000]
        s = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        for ni in n:
            if num < ni:
                return s[n.index(ni) - 1], n[n.index(ni) - 1]

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        r = ''
        while num != 0:
            ss, n = Solution().index_n(num)
            r = r + ss
            num = num - n
        return r
# for i in range(int(input())):
print(Solution().intToRoman(int(input())))