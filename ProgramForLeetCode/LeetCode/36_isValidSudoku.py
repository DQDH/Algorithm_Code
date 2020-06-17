class Solution(object):
    def isValidSudoku1(self, board):
        row = [set([]) for i in range(9)]
        col = [set([]) for i in range(9)]
        grid = [set([]) for i in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row[r]:
                    return False
                if board[r][c] in col[c]:
                    return False

                g = int(r / 3 * 3 + c / 3)
                if board[r][c] in grid[g]:
                    return False
                grid[g].add(board[r][c])
                row[r].add(board[r][c])
                col[c].add(board[r][c])
        return True
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        m=9
        for i in range(m):
            l1=''.join(board[i]).replace('.','')
            if len(set(l1))!=len(l1):
                return False
        for p in range(0,m,3):
            for q in range(0,m,3):
                l1 = ''.join([''.join(board[k][q:q + 3]) for k in range(p,p+3)]).replace('.', '')
                if len(set(l1)) != len(l1):
                    return False
        for j in range(m):
            l1=''.join([board[k][j] for k in range(m)]).replace('.', '')
            if len(set(l1))!=len(l1):
                return False
        return True
print(Solution().isValidSudoku1([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))