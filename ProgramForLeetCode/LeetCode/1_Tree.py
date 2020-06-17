# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def InitTree(self,matrix):
        if len(matrix)<1:
            return TreeNode(None)
        root=TreeNode(matrix[0])
        NodeQueen=[root]
        root_i=0
        index=1
        while index<len(matrix):
            node=NodeQueen[root_i]
            root_i+=1
            # if matrix[index] !="null":
            node.left=TreeNode(matrix[index])
            NodeQueen.append(node.left)
            index+=1
            if index>=len(matrix):
                break
            # if matrix[index] !="null":
            node.right=TreeNode(matrix[index])
            NodeQueen.append(node.right)
            index+=1
        return root
    def Print(self,Root):
        print(Root.val)
        if Root.left:
            self.Print(Root.left)
        if Root.right:
            self.Print(Root.right)
R1=TreeNode(None).InitTree([1,2,3])
R2=TreeNode(None).InitTree([1,2,3,4,5])
TreeNode(None).Print(R1)
TreeNode(None).Print(R2)