#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]*n
        a = 0
        b = 0
        c = 0
        for i in range(1,n):
            dp[i] = min(dp[a]*2, dp[b]*3, dp[c]*5)
            if dp[i]==dp[a]*2:
                a += 1
            if dp[i]==dp[b]*3:
                b += 1
            if dp[i]==dp[c]*5:
                c += 1
        return dp[-1]
# @lc code=end

