#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        res = 0
        for j in range(1,len(prices)):
            if prices[j]>prices[j-1]:
                res += prices[j]-prices[j-1]
        return res
        
# @lc code=end

