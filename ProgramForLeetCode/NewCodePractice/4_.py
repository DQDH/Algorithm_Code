#红包：双指针，分别从两端开始计算第一部分和第三部分的和，
# 如果出现相等，则返回第一部分的和，否则，根据两部分和的大小判断哪个指针移动，
# 直到出现第一部分和第三部分相等。若无可以拆分的情况，返回0
class solution(object):
    def Q(self,nums):
        if len(nums)<2:
            return 0
        if len(nums)==2 or len(nums)==3:
            if nums[0]==nums[-1]:
                return nums[0]
            else:
                return 0
        l,r=1,len(nums)-2
        l_sum=nums[0]
        r_sum=nums[len(nums)-1]
        while l<r:
            if l_sum==r_sum:
                return l_sum
            if l_sum<r_sum:
                l+=1
                l_sum+=nums[l]
            else:
                r+=1
                r_sum+=nums[r]
        return 0

nums = [1,2,2]
print(solution().Q(nums))