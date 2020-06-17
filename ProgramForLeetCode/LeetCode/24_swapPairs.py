class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def InitListNode(self,matrix):
        if len(matrix)==0:
            return ListNode(None)
        head=p=ListNode(matrix[0])
        for num in matrix[1:]:
            p.next=ListNode(num)
            p=p.next
        return head
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p=head
        if not head :
            return head
        if not head.next:
            return head

        save=head.next
        head.next=head.next.next
        save.next=head
        head=save
        p=head.next
        while p.next:
            save=p.next
            if save.next:
                p.next=p.next.next
                save.next=save.next.next
                p.next.next=save
                p=p.next.next
            else:
                return head
        return head
head=Solution().swapPairs(ListNode(None).InitListNode([1,2,3,4,1]))
while head:
    print(head.val)
    head=head.next
