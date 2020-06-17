class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        t=prices[0]
        re=0
        for p in prices:
            if p>t:
                re=re+(p-t)
                t=p
            else:
                t=p
        return re
Solution().maxProfit([])