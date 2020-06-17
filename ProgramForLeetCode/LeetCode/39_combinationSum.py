class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()

        def dfs(remain, path):
            if not remain:
                res.append(path)
                return
            for i in candidates:
                if i > remain:
                    break
                elif path and i < path[-1]:
                    continue
                else:
                    dfs(remain - i, path + [i])

        dfs(target, [])
        return res
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def helper(remain, combi, idx):
            if remain < 0:
                return
            if remain == 0:
                res.append(combi)
                return
            if idx >= len(candidates):
                return
            helper(remain, combi, idx + 1)
            helper(remain - candidates[idx], combi + [candidates[idx]], idx)

        res = []
        helper(target, [], 0)
        return res
print(Solution().combinationSum([10,2,7,6,5],8))