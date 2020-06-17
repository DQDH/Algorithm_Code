class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res=int(bin(n)[2:].zfill(32)[::-1],2)
        return res
Solution().reverseBits(6)