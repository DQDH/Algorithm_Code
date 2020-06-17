class LNK(str):
    def __lt__(x, y):
        return x + y > y + x
class Solution(object):
    def Q1(self,nums):
        res = ''.join(sorted(map(str, nums), key=LNK))
        return '0' if res[0]=='0' else res
nums=list(map(int,input().split(',')))
print(Solution().Q1(nums))