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
        p.next=self.head.next
        return self.head
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head :
            return False
        lookup={}
        while head:
            if head in lookup:
                return True
            else:
                lookup[head]=1
                head=head.next
        return False
    def hasCycle1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
l=ListNode(None).InitListNode([3,2,0,-4])
a=Solution().hasCycle1(l)
b=1
