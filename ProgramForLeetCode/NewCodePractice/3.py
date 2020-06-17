'''
https://www.nowcoder.com/questionTerminal/83b419c027fa490aa60669b0e7dc06a3
又到了丰收的季节，恰逢小易去牛牛的果园里游玩。
牛牛常说他对整个果园的每个地方都了如指掌，小易不太相信，所以他想考考牛牛。
在果园里有N堆苹果，每堆苹果的数量为ai，小易希望知道从左往右数第x个苹果是属于哪一堆的。
牛牛觉得这个问题太简单，所以希望你来替他回答。

'''
class solution(object):
    def find_num(self,n,nums,m,que):
        for i in range(m):
            target=que[i]
            for j in range(n):
                if target<sum(nums[:i+1]):
                    print(j)
        # for i in range(1,n):
        #     nums[i]+=nums[i-1]
        # for j in range(m):
        #     target=que[j]
        #     for i in range(n-1,-1,-1):
        #         if nums[i-1]<target<=nums[i]:
        #             print(i+1)
n=int(input())
nums=list(map(int,input().split()))
m=int(input())
que=list(map(int,input().split()))
solution().find_num(n,nums,m,que)