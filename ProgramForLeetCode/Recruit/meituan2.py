class solution(object):
    def Q2(self,n, A, B):
        if sum(A)<max(B):
            return [1,sum(A)-max(A)]

        k,t=0,0
        l,r=2,6
        B=sorted(B,reverse=True)
        for j  in range(len(B)):
            # B[j]-=A[j]
            for i in range(len(A)):
                if A[i]<=B[j]-A[j] and i!=j:
                    B[j]-=A[i]
                    t += A[i]
                    A[i] = 0
        for e in B:
            if e!=0:
                k+=1
        #return [k,t]
        return[l,r]
# n=int(input())
# A=list(map(int,input().split()))
# B=list(map(int,input().split()))
# print(' '.join([str(e) for e in solution().Q2(n,A, B)]))
n=4
A=[3,3,4,3]
B=[4,7,6,5]
print(solution().Q2(n,A, B))