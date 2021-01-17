#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 递推式考虑冷冻期长
        if len(prices)==0:
            return 0
        dp = [[0,0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            if i-2<0:
                temp = 0
            else:
                temp = dp[i-2][0]
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], temp-prices[i])
        return dp[-1][0]
# @lc code=end

