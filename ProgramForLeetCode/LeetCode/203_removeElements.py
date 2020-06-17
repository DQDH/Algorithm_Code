# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def InitListNode(self,matrix):
        self.head=ListNode(matrix[0])
        p=self.head
        for num in matrix[1:]:
            p.next=ListNode(num)
            p=p.next
        return self.head
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        res=res1=ListNode(0)
        while head:
            if head.val!=val:
                res1.next=head
                res1=res1.next
            head=head.next
        res1.next=None
        return res.next
l=ListNode(None).InitListNode([1,2,1,1])
Solution().removeElements(l,1)
