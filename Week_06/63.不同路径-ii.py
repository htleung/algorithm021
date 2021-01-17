#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1]==1 or obstacleGrid[0][0]==1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(1,m):
            if obstacleGrid[i][0]==1:
                dp[i][0] = 0
            else:
                dp[i][0] = min(dp[i-1][0], 1)
        for j in range(1,n):
            if obstacleGrid[0][j]==1:
                dp[0][j] = 0
            else:
                dp[0][j] = min(dp[0][j-1], 1)
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
# @lc code=end

