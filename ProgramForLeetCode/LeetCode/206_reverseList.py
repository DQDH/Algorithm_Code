class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def InitListNode(self,matrix):
        head=ListNode(None)
        p=head
        for i in matrix:
            p.next=ListNode(i)
            p=p.next
        return head.next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def helper(head, new_head):
            if head:
                nxt = head.next
                head.next = new_head
                return helper(nxt, head)
            else:
                return new_head
        return helper(head, None)
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        while not head or not head.next:
            return head
        p=head
        while p.next:
            q=p.next
            p.next=p.next.next
            q.next=head
            head=q
        return head
l=ListNode(None).InitListNode([1,2,3])
l1=Solution().reverseList(l)
while l1:
    print(l1.val)
    l1=l1.next