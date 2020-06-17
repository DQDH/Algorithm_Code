class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        f=ListNode(0)
        s=ListNode(0)
        r1=f
        r2=s
        while head:
            if head.val<x:
                f.next=head
                f=f.next
            else:
                s.next=head
                s=s.next
            head=head.next
        f.next=None
        s.next=None
        f.next=r2.next
        return r1.next