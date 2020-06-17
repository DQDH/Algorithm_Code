class Solution:
    def isValid1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        if len(s) == 0:
            return True
        ss1 = ['(', ')', '{', '}', '[', ']']
        for i in range(0,6,2):
            if s.count(ss1[i])!=s.count(ss1[i+1]):
                return False
        while '()' in s or '[]' in s or '{}' in s:
            s=s.replace('()','')
            s=s.replace('[]','')
            s=s.replace('{}','')
        if s=='':
            return True
        else:
            return False

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftP = '([{'
        rightP = ')]}'
        stack = []
        for char in s:
            if char in leftP:
                stack.append(char)
            if char in rightP:
                if not stack:
                    return False
                tmp = stack.pop()
                if char == ')' and tmp != '(':
                    return False
                if char == ']' and tmp != '[':
                    return False
                if char == '}' and tmp != '{':
                    return False
        return stack == []
Solution().isValid("()[]{}")