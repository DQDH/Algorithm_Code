# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def InintListNode(self,matrix):
        head=p=ListNode(matrix[0])
        for num in matrix[1:]:
            p.next=ListNode(num)
            p=p.next
        return head
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p=q=head
        k=0
        while p:
            if k<n+1:
                p=p.next
            else:
                p=p.next
                q=q.next
            k=k+1
        if n<=k:
            q.next=q.next.next
        else:
            return False
        return head
print(Solution().removeNthFromEnd(ListNode(None).InintListNode([1,2,3,4,5]),2))
