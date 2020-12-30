#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j, grid, m, n):
            if grid[i][j]=='0' or i<0 or i>=m or j<0 or j>=n:
                return
            grid[i][j] = '0'
            if i-1>=0:
                dfs(i-1, j, grid, m, n)
            if i+1<m:
                dfs(i+1, j, grid, m, n)
            if j-1>=0:
                dfs(i, j-1, grid, m, n)
            if j+1<n:
                dfs(i, j+1, grid, m, n)
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    count += 1
                dfs(i, j, grid, m, n)
        return count
# @lc code=end

