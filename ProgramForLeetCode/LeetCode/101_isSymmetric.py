class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def InitTree(self,matrix):
        root=TreeNode(matrix[0])
        nodequeue=[root]
        front=0
        index=1
        while index < len(matrix):
            node=nodequeue[front]
            front+=1
            if matrix[index] != None:
                node.left=TreeNode(matrix[index])
                nodequeue.append(node.left)
            index+=1
            if index>=len(matrix):
                break
            if matrix[index]!=None:
                node.right=TreeNode(matrix[index])
                nodequeue.append(node.right)
            index += 1
        return root

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.symmetric(root.left, root.right)

    def symmetric(self, l1, l2):
        if not l1 and not l2:
            return True
        elif l1 and l2 and l1.val == l2.val:
            return self.symmetric(l1.left, l2.right) and self.symmetric(l1.right, l2.left)
        else:
            return False
p=TreeNode(None).InitTree([1,2,2,None,3,3])
print(Solution().isSymmetric(p))