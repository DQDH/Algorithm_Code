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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res=head
        while head:
            while head.next and head.val==head.next.val:
                head.next=head.next.next
            head=head.next
        return res
l=ListNode(-1).InitListNode([1,1,1])
Solution().deleteDuplicates(l)