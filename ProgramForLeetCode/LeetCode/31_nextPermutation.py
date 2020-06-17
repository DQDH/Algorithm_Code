# class Solution(object):
#     def nextPermutation(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         if len(nums) <= 1:
#             return
#         idx = 0
#         for i in range(len(nums)-1, 0, -1):
#             if nums[i] > nums[i-1]: # find first number which is smaller than it's after number
#                 idx = i
#                 break
#         if idx != 0: # if the number exist,which means that the nums not like{5,4,3,2,1}
#             for i in range(len(nums)-1, idx-1, -1):
#                 if nums[i] > nums[idx-1]:
#                     nums[i], nums[idx-1] = nums[idx-1], nums[i]
#                     break
#
#         nums[idx:] = nums[idx:][::-1]
class Solution(object):
    def reverse(self,num):
        for i in range(int(len(num)/2)):
            tmp=num[i]
            num[i]=num[len(num)-1-i]
            num[len(num)-1-i]=tmp
        return num
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        id=0
        length=len(nums)
        for i in range(length-1,0,-1):
            if nums[i]>nums[i-1]:
                j = length-1
                while j>=i:
                    if nums[i-1]<nums[j]:
                        tmp=nums[i-1]
                        nums[i-1]=nums[j]
                        nums[j]=tmp
                        break
                    j-=1
                id=i
                break
        nums[id:] = self.reverse(nums[id:])
        print(nums)
Solution().nextPermutation([3,2,1])
#1,5,8,4,7,6,5,3,1
