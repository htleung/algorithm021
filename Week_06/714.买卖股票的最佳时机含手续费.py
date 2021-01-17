#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices)==0:
            return 0
        dp = [[0,0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee)
        return dp[-1][0]
# @lc code=end

