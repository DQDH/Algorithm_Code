class Solution(object):
    def combinationSum21(self, candidates, target):
        res = []
        candidates.sort()

        def backtrack(remain, temp, start):
            if not remain:
                res.append(temp[:])
            else:
                for i in range(start, len(candidates)):
                    if candidates[i] > remain:
                        break
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    n = candidates[i]
                    backtrack(remain - n, temp + [n], i + 1)

        backtrack(target, [], 0)
        return res

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []

        def next(remain, path, candidate):
            if remain == 0 and path not in res:
                res.append(path)
                return
            i = 0
            while i < len(candidate):
                if candidate[i] > remain:
                    break
                else:
                    next(remain - candidate[i], path + [candidate[i]], candidate[i + 1:])
                i += 1

        next(target, [], candidates)
        return res
print(Solution().combinationSum21([10,1,2,7,6,1,5],8))