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
h=ListNode(None).InitListNode([])
while h:
    print(h.val)
    h=h.next