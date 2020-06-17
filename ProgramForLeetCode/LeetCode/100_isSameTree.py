# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def InitTree(self,matrix):
        root=TreeNode(matrix[0])
        nodeQueue = [root]
        front = 0
        index = 1
        while index < len(matrix):
            node = nodeQueue[front]
            front = front + 1
            leftNumber = matrix[index]
            index = index + 1
            if leftNumber != "null":
                node.left = TreeNode(leftNumber)
                nodeQueue.append(node.left)
            if index >= len(matrix):
                break
            rightNumber = matrix[index]
            index = index + 1
            if rightNumber != "null":
                node.right = TreeNode(rightNumber)
                nodeQueue.append(node.right)
        return root
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif p and q and p.val==q.val:
            if self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
                return True
            else:
                return False
        else:
            return False
p=TreeNode(None).InitTree([1,2,3,4,5])
q=TreeNode(None).InitTree([1,2,3])
print(Solution().isSameTree(p,q))
