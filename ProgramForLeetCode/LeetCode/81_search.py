class Solution(object):
    def search(self, nums, target):
        if not nums or len(nums) == 0:
            return False
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return True
            if nums[l] < nums[m]:
                if target >= nums[l] and target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            elif nums[m] < nums[l]:
                if target >= nums[m] and target <= nums[r]:
                    l = m
                else:
                    r = m - 1
            else:
                l += 1
        return False