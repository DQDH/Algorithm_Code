class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        currentmin=self.getMin()
        if currentmin==None or x<currentmin:
            currentmin=x
        self.lst.append((x,currentmin))
    def pop(self):
        """
        :rtype: void
        """
        self.lst.pop()
    def top(self):
        """
        :rtype: int
        """
        return self.lst[-1][0]
    def getMin(self):
        """
        :rtype: int
        """
        if len(self.lst)==0:
            return None
        else:
            return self.lst[len(self.lst)-1][1]
# class MinStack(object):
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.lst = []
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: void
#         """
#         self.lst.append(x)
#     def pop(self):
#         """
#         :rtype: void
#         """
#         self.lst.pop()
#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.lst[-1]
#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return min(self.lst)
# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3,param_4)
