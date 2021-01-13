#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1)==0 or len(word2)==0:
            return max(len(word1), len(word2))
        m = len(word1)
        n = len(word2)
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            if word1[i] == word2[0]:
                dp[i][0] = i
            else:
                if i==0:
                    dp[i][0] = 1
                else:
                    dp[i][0] = min(dp[i-1][0]+1, i+1)
        for j in range(n):
            if word2[j] == word1[0]:
                dp[0][j] = j
            else:
                if j==0:
                    dp[0][j] = 1
                else:
                    dp[0][j] = min(dp[0][j-1]+1, j+1)
        for i in range(1,m):
            for j in range(1,n):
                if word1[i] == word2[j]:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]
# @lc code=end

