class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def Init(self,matrix):
        head=ListNode(None)
        p=head
        for i in matrix:
            p.next=ListNode(i)
            p=p.next
        return head.next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
       """
        if not head or k==0:
            return head
        p=q=head
        length=1
        while q.next:
            length+=1
            q=q.next
        q.next=p
        n=length-k%length
        while n-1:
            p=p.next
            n-=1
        head=p.next
        p.next=None
        return head
    def rotateRight1(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
       """
        if not head or k==0:
            return head
        p=q=head
        n=1
        t=k
        flag=1
        while flag:
            while q.next:
                n+=1
                if t>0:
                    q=q.next
                    t-=1
                else:
                    q=q.next
                    p=p.next
            if k<n:
                flag=0
            else:
                k=k%n
                if k==0:
                    return head
                t=k
                p=q=head
        q.next = head
        head=p.next
        p.next=None
        return head
l=ListNode(None).Init([1,2,3,4,5])
res=Solution().rotateRight(l,2)
while res:
    print(res.val)
    res=res.next
