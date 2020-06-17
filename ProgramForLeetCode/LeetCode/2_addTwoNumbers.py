# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def InitListNode(self,matrix):
        head=ListNode(matrix[0])
        p=head
        for num in matrix[1:]:
            p.next=ListNode(num)
            p=p.next
        return head
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res=res1=ListNode(0)
        On_num=0
        while l1 and l2:
            num=l1.val + l2.val+On_num
            if num>9:
                res1.next=ListNode(num%10)
                On_num=1
            else:
                res1.next=ListNode(num)
                On_num=0
            l1=l1.next
            l2=l2.next
            res1=res1.next

        while l1:
            num=l1.val+On_num
            if num>9:
                On_num=1
            else:
                On_num=0
            res1.next = ListNode(num%10)
            l1=l1.next
            res1=res1.next
        while l2:
            num=l2.val+On_num
            if num>9:
                On_num=1
            else:
                On_num=0
            res1.next = ListNode(num%10)
            l2=l2.next
            res1=res1.next
        if On_num == 1:
            res1.next = ListNode(1)
        return res.next
l1=ListNode(None).InitListNode([1])
l2=ListNode(None).InitListNode([9,9])
Solution().addTwoNumbers(l1,l2)