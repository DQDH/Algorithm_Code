# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def InitListNode(self,matrixa,matrixb,skipa,skipb):
        heada=ListNode(matrixa[0])
        pa=heada
        for numa in matrixa[1:skipa]:
            pa.next=ListNode(numa)
            pa=pa.next
        headb=ListNode(matrixb[0])
        pb=headb
        for numb in matrixb[1:skipb]:
            pb.next=ListNode(numb)
            pb=pb.next
        head=ListNode(matrixb[skipb])
        p=head
        for num in matrixb[skipb+1:]:
            p.next=ListNode(num)
            p = p.next
        pa.next=head
        pb.next=head
        return heada,headb
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        '''
        在这里注意AB两个链表的长度是不相同的，但是如果分别以A、B为起始，连续读取两个链表，读取到的长度是相同的。
        如果在尾部有重复的部分,我们可以这样看两个链表：A=a+c、B=b+c（前半部分不同，后半部分相同）。
        所以我们此时两次读取到的链表分别是a+c+b+c以及b+c+a+c。可以发现，两次读取最后的部分是相同的。
        如果两个链表没有重复的部分，按照上面的方式读取完之后，下一个值（.next）都是None，也是相同的。
        所以我们可以将两个节点是否相等作为循环条件，如果不相等就继续循环，往下读；如果相等的话就返回当前值。
        此时返回值有可能是重复部分的第一个值，也有可能是None。符合要求。
        '''
        pA, pB = headA, headB
        while pA is not pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
        #chaoshi
        # p=headB
        # while headA:
        #     headB=p
        #     while headB:
        #         if headA==headB:
        #             return headA.val
        #         else:
        #             headB=headB.next
        #     headA=headA.next
        # return headA
l1,l2=ListNode(None).InitListNode([4,1,8,4,5],[5,0,1,8,4,5],2,3)
Solution().getIntersectionNode(l1,l2)