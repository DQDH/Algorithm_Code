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
class solution(object):
    def Q1(self,head):
        s1 = 0
        s2 = 0
        n = 1
        while head != None:
            s1 = s1 * 10 + head.val
            s2 = s2 + n * head.val
            n = n * 10
            head = head.next
        return s1 == s2
data = list(map(int, input().split(' ')))
head = ListNode(0).InitListNode(data)
print(solution().Q1(head))

