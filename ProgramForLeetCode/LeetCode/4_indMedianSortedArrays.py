class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1=len(nums1)
        n2=len(nums2)
        midnum=round((n1+n2)/2.0+0.2)
        reslist=[]
        flag=0
        if (n1+n2)%2==1:
            flag=1
            midnum=midnum-1
        if not (n1 and n2):
            reslist=reslist+nums1+nums2
            if flag == 0:
                return (reslist[int(midnum)] + reslist[int(midnum - 1)]) / 2.0
            else:
                return reslist[int(midnum)]
        else:
            i, j, k = 0, 0, 0
            while k < midnum + 1:
                if i > n1 - 1:
                    reslist = reslist + nums2[j:]
                    if flag == 0:
                        return (reslist[int(midnum)] + reslist[int(midnum - 1)]) / 2.0
                    else:
                        return reslist[int(midnum)]
                if j > n2 - 1:
                    reslist = reslist + nums1[i:]
                    if flag == 0:
                        return (reslist[int(midnum)] + reslist[int(midnum - 1)]) / 2.0
                    else:
                        return reslist[int(midnum)]
                if nums1[i] > nums2[j]:
                    reslist.append(nums2[j])
                    j = j + 1
                else:
                    reslist.append(nums1[i])
                    i = i + 1
                k = k + 1
            if flag == 0:
                return (reslist[-2] + reslist[- 1]) / 2.0
            else:
                return reslist[- 1]
a=Solution().findMedianSortedArrays([1,2],[3,4])
print(a)