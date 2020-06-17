class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def InitTreeNode(self,matrix):
        if len(matrix)<1:
            return TreeNode(matrix[0])
        else:
            root=TreeNode(matrix[0])
            Nodequeen=[root]
            root_i=0
            index=1
            while index<len(matrix):
                root=Nodequeen[root_i]
                root_i+=1
                root.left=TreeNode(matrix[index])
                Nodequeen.append(root.left)
                index+=1
                if index>=len(matrix):
                    break
                root.right=TreeNode(matrix[index])
                Nodequeen.append(root.right)
                index+=1
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
p=TreeNode(None).InitTreeNode([1,2,2,3,3,3,3])
print(Solution().isSymmetric(p))