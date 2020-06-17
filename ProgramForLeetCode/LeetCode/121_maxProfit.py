class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        t=prices[0]
        r=0
        for n in prices:
            if n>t:
                r=max(r,n-t)
            else:
                t=n
        return r
Solution().maxProfit([2,4,1])
