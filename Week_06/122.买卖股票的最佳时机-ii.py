#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心算法
        # if len(prices)<2:
        #     return 0
        # res = 0
        # for j in range(1,len(prices)):
        #     if prices[j]>prices[j-1]:
        #         res += prices[j]-prices[j-1]
        # return res
        
        # 动态规划
        dp=[[0]*2 for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        return dp[-1][0]
# @lc code=end

