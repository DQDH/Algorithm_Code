# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x=None):
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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        res1=res=ListNode(-1)
        while l1 and l2:
            if l1.val<l2.val:
                res.next=l1
                l1=l1.next
            else:
                res.next=l2
                l2=l2.next
            res=res.next
        res.next=l1 if l1 else l2
        return res1.next

l1=ListNode().InitListNode([1,2,4])
l2=ListNode().InitListNode([3,5,6])
h=Solution().mergeTwoLists(l1,l2)
while h:
    print(h.val)
    h=h.next
# a=1
# print('input')
# a=input()
# while a!='\n':
#     ListNode(a)