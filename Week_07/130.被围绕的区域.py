#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #dfs
        # if not board: return 
        # def dfs(i, j):
        #     if not 0<=i<m or not 0<=j<n or board[i][j]!='O':
        #         return 
        #     board[i][j] = 'A'
        #     dfs(i+1, j)
        #     dfs(i-1, j)
        #     dfs(i, j+1)
        #     dfs(i, j-1)

        # m = len(board)
        # n = len(board[0])
        # for i in range(m):
        #     dfs(i,0)
        #     dfs(i,n-1)
        # for j in range(n):
        #     dfs(0, j)
        #     dfs(m-1,j)
        
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j]=='A':
        #             board[i][j] = 'O'
        #         elif board[i][j]=='O':
        #             board[i][j] = 'X'
        
        #并查集
        if not board or not board[0]:
            return
        f = {}
        def parent(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = parent(f[x])
            return f[x]
        def union(x, y):
            f[parent(y)] = parent(x)
        row = len(board)
        col = len(board[0])
        dummy = row*col #用dummy作为与边界O连通的所有O的标记
        for i in range(row):
            for j in range(col):
                if board[i][j]=='O':
                    if i==0 or i==row-1 or j==0 or j==col-1:
                        union(i*col+j, dummy)
                    else:
                        for x,y in ((i+1,j), (i-1, j), (i,j+1), (i,j-1)):
                            if board[x][y]=='O':
                                union(i*col+j, x*col+y)
        for i in range(row):
            for j in range(col):
                if parent(i*col+j)==parent(dummy):
                    board[i][j]='O'
                else:
                    board[i][j]='X'
# @lc code=end

