class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        tmp_node=ListNode(0)
        tmp_node.next=head
        head=tmp_node
        while head.next and head:
            begin=head.next
            if begin.next and begin.next.val==begin.val:
                end=begin.next
                while end.next and end.val==end.next.val:
                    end=end.next
                head.next=end.next
            else:
                head=head.next
        return tmp_node.next