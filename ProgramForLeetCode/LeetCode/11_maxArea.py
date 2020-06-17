class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res=0
        i=0
        j=len(height)-1
        while i<=j:
            area=min(height[i],height[j])*(j-i)
            res=max(area,res)
            if height[i]<height[j]:
                i=i+1
            elif height[i]>height[j]:
                j=j-1
            else:
                i=i+1
                j=j-1
        return res
Solution().maxArea([1,8,6,2,5,4,8,3,7])