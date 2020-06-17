class queueTostack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        if self.queue2:
            self.queue2.append(x)
        else:
            self.queue1.append(x)
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.queue2:
            self.queue2=self.queue1[:-1]
            res=self.queue1[-1]
            self.queue1=[]
        else:
            self.queue1 = self.queue2[:-1]
            res=self.queue2[-1]
            self.queue2 = []
        return res
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue1[-1] if self.queue1 else self.queue2[-1]
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if not (self.queue1 or self.queue2):
            return True
        return False
obj = queueTostack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.pop()
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2,param_3,param_4)