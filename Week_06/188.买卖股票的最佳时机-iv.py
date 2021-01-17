#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 增加一个长为k的维度，记录已经完成的交易次数
        n = len(prices)
        if n==0 or k==0:
            return 0
        if k>n//2:
            profit = 0
            for i in range(1,n):
                if prices[i]>prices[i-1]:
                    profit += prices[i]-prices[i-1]
            return profit
        dp = [[[0,0] for _ in range(k)] for _ in range(n)]
        for j in range(k):
            dp[0][j][1] = -prices[0]
        for i in range(1,n):
            for j in range(k):
                if j==0:
                    dp[i][j][1] = max(dp[i-1][j][1], 0-prices[i])
                else:
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
        return dp[n-1][k-1][0]
# @lc code=end

