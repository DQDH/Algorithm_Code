class Solution(object):
    def lengthOfLongestSubstring(self, s):
            """
            :type s: str
            :rtype: int
            """
            num=1
            if len(s) < 2:
                return len(s)
            else:
                for i in range(len(s)):
                    for j in range(i+2,len(s)+1):
                        ss=s[i:j]
                        if len(set(s[i:j]))==len(s[i:j]):
                            if len(s[i:j])>num:
                                num=len(s[i:j])
                        else:
                            break
            return num

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashes = {}
        left, right, length = 0, 0, len(s)
        max_len = 0
        while right < length:
            if hashes.get(s[right]) and hashes[s[right]] >= left:
                left = hashes[s[right]]
            hashes[s[right]] = right + 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len


    def lengthOfLongestSubstring3(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length < 2:
            return length

        max_len = 1
        for i in range(0, length - 1):
            l = 1
            # print('i', i, 'l', l, 's[i+l]', s[i+l], 's[i:i+l+1]', s[i:i+l])
            while (i + l < length) and (s[i + l] not in s[i:i + l]):
                l += 1
            max_len = max(max_len, l)
        return max_len

    def lengthOfLongestSubstring4(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        left = 0
        last = {}
        for i in range(len(s)):
            if s[i] in last and last[s[i]] >= left:
                left = last[s[i]] + 1
            last[s[i]] = i
            ans = max(ans, i - left + 1)
        return

    def lengthOfLongestSubstring5(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = start = 0
        for i in range(len(s)):
            if s[i] in s[start: i]:
                start = s.index(s[i], start) + 1
            else:
                maxLength = max(maxLength, i - start + 1)
        return maxLength
s="uqinntq"
a=Solution().lengthOfLongestSubstring0(s)
print(a)