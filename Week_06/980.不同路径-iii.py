#
# @lc app=leetcode.cn id=980 lang=python3
#
# [980] 不同路径 III
#

# @lc code=start
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(path, i, j, grid, m, n, total):
            nonlocal ans
            if grid[i][j]==2 and len(path)==total:
                ans += 1
                return
            if i-1>=0 and (i-1,j) not in path and grid[i-1][j]!=-1:
                path.append((i-1,j))
                dfs(path, i-1, j, grid, m, n, total)
                path.pop()
            if i+1<m and (i+1,j) not in path and grid[i+1][j]!=-1:
                path.append((i+1,j))
                dfs(path, i+1, j, grid, m, n, total)
                path.pop()
            if j-1>=0 and (i,j-1) not in path and grid[i][j-1]!=-1:
                path.append((i,j-1))
                dfs(path, i, j-1, grid, m, n, total)
                path.pop()
            if j+1<n and (i, j+1) not in path and grid[i][j+1]!=-1:
                path.append((i,j+1))
                dfs(path, i, j+1, grid, m, n, total)
                path.pop()
        m = len(grid)
        n = len(grid[0])
        start = (0,0)
        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=-1:
                    total+=1
                if grid[i][j]==1:
                    start = (i,j)
        ans = 0
        path = [start]
        dfs(path, start[0], start[1], grid, m, n, total)
        return ans
        
# @lc code=end

