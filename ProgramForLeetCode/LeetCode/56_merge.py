class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def Init(self,matrix):
        res=[]
        for m in matrix:
            res.append(Interval(m[0],m[1]))
        return res
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        for i in sorted(intervals, key=lambda x: x.start):
            if res and i.start <= res[-1].end:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res.append(i)
        return res
    def merge1(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        i=1
        while i < len(intervals):
            if intervals[i].start in range(intervals[i-1].start,intervals[i-1].end+1):
                intervals[i].start=intervals[i-1].start
                intervals[i].end=max(intervals[i-1].end,intervals[i].end)
                intervals.remove(intervals[i-1])
                i-=1
            i+=1
        return intervals
Interval1=Interval().Init([[1,4],[0,4]])
print(Solution().merge(Interval1))