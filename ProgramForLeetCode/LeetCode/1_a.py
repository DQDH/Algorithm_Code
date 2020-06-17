# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def InitListNode(self,matrix):
        if len(matrix)<1:
            return ListNode(None)
        head=ListNode(matrix[0])
        p=head
        for num in matrix[1:]:
            p.next=ListNode(num)
            p=p.next
        return head
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head and not head.next:
            return head
        tmp=ListNode(0)
        tmp.next=head;head=tmp
        while head:
            if head.next:
                tmp=head.next
            if head.next.next and head.next.val==head.next.next.val:
                head
l=ListNode(None).InitListNode([1,1,1,2,2,3,4,5,5])
h=Solution().deleteDuplicates(l)
while h:
    print(h.val)
    h=h.next