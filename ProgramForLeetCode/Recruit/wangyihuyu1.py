# t=1
# n=5
# nums=[8,3,5,7,2]
class solution(object):
    def get_classes(self,nums ):
        classes=[]
        for ni in nums:
            d2b=[int(e) for e in list(str(bin(ni))[2:])]
            class_i=sum(d2b)
            if class_i not in classes:
                classes.append(class_i)
        return len(classes)
t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(solution().get_classes(nums))