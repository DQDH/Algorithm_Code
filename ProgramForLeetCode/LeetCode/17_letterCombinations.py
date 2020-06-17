class Solution(object):
    def combine(self,list1,list2):
        list=[]
        for i in list1:
            for j in list2:
                list.append(i+j)
        return list
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        length=len(digits)
        if length==0:
            return digits
        if length<2:
            return list(dict[digits[0]])
        # digits=[each for each in map(int ,list(digits))]
        digits=list(digits)
        list1 = list(dict[digits[0]])
        list2 = list(dict[digits[1]])
        for i in range(1,length):
            list1=Solution().combine(list1,list2)
            if i+1<length:
                list2=list(dict[digits[i+1]])
        return list1
print(Solution().letterCombinations('2'))