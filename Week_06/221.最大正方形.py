#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1],dp[i-1][j-1]) + 1
        ma = max([max(line) for line in dp])
        return ma*ma
# @lc code=end

