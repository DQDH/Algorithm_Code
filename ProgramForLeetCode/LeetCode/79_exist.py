class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def helper(i,j,k):
            if not 0<=i<=row-1 or not 0<=j<=col-1 or board[i][j]!=word[k]:
                return False
            elif k==len(word)-1:
                return True
            else:
                board[i][j]='*'
                res=helper(i-1,j,k+1) or helper(i,j+1,k+1) or helper(i+1,j,k+1) or helper(i,j-1,k+1)
                board[i][j]=word[k]
                return res
        if not board:
            return False
        if not word:
            return True
        row = len(board)
        col = len(board[0])
        if row * col < len(word):
            return False
        for i in range(row):
            for j in range(col):
                if helper(i,j,0):
                    return True
        return False
print(Solution().exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
],"ABCCED"))