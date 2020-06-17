class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        t=m-2
        for nums in nums2:
            t = t + 1
            if nums <= nums1[0]:
                nums1[1:t+2] = nums1[0:t+1]
                nums1[0] = nums
            elif nums >= nums1[t]:
                nums1[t+1] = nums
            else:
                for i in range(t):
                    if nums==nums1[i]:
                        nums1[i + 2:t + 2] = nums1[i + 1:t + 1]
                        nums1[i + 1] = nums
                        break
                    if nums >= nums1[i] and nums <= nums1[i + 1]:
                        nums1[i + 2:t + 2] = nums1[i + 1:t + 1]
                        nums1[i + 1] = nums
                        break
    def merge2(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        t = m - 2
        for nums in nums2:
            t = t + 1
            if nums <= nums1[0]:
                nums1.insert(0, nums)
            elif nums >= nums1[t]:
                nums1.insert(t + 1, nums)
            else:
                for i in range(len(nums1) - 1):
                    if nums == nums1[i]:
                        nums1.insert(i, nums)
                        break
                    elif nums == nums1[i + 1]:
                        nums1.insert(i + 1, nums)
                        break
                    elif nums > nums1[i] and nums < nums1[i + 1]:
                        nums1.insert(i + 1, nums)
                        break
            del nums1[-1]
nums1 = [2,0]
m = 1
nums2 = [1]
n =1
Solution().merge(nums1,m,nums2,n)
