class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend > 0) is (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp, num = divisor, 1
            while dividend >= tmp:
                num <<= 1
                tmp <<= 1
            dividend -= tmp >> 1
            res += num >> 1
        res = res if positive else -res
        return min(max(-(2**31), res), 2**31-1)
print(Solution().divide(39,5))