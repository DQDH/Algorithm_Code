class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        result=[]
        strnum=str(numbers)
        for i in range(len(numbers)):
            if numbers[i]<=target:
                other=target-numbers[i]
                if other in numbers:
                    result.append(i+1)
                    result.append(numbers.index(other)+1)
                    if result[0]==result[1]:
                        numbers[result[0]-1]=numbers[result[0]-1]+1
                        if other in numbers:
                            result[1]=numbers.index(other)+1
                        else:
                            result=[]
                    return result
        return result
Solution().twoSum([3,4,0,0],0)