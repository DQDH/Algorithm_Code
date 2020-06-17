class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length=len(nums)
        if not nums or length==0:
            return [-1,-1]
        l,r=0,length-1
        res=[]
        while l<=r:
            mid=int((l+r)/2)
            if nums[mid]==target and (nums[mid-1]!=target or mid==0):
                res.append(mid)
                break
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        if len(res)==0:
            return [-1,-1]
        l,r=res[0],length-1
        while l<=r:
            mid = int((l + r) / 2)
            if nums[mid]==target:
                if mid==length-1:
                    res.append(mid)
                    break
                elif nums[mid+1]!=target:
                    res.append(mid)
                    break
            if nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return res
print(Solution().searchRange([7],7))