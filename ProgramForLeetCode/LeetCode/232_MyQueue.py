class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst1 = []
        self.lst2 = []
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.lst1.append(x)
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.lst2:
            while self.lst1:
                self.lst2.append(self.lst1.pop())
        return self.lst2.pop()
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.lst2:
            return self.lst2[-1]
        else:
            while self.lst1:
                self.lst2.append(self.lst1.pop())
            return self.lst2[-1]
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if not self.lst2:
            if not self.lst1:
                return True
        return False
obj = MyQueue()
obj.push(1)
obj.push(2)
param_3 = obj.peek()
param_2 = obj.pop()
param_4 = obj.empty()
print(param_2,param_3,param_4)