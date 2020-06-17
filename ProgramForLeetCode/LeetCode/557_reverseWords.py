class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([k[::-1] for k in s.split()])
print(Solution().reverseWords("Let's take LeetCode contest"))