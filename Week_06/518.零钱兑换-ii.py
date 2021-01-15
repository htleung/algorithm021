#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #dp[i][j]:使用硬币coins[0..i]组成金额j的组合数
        if amount==0:
            return 1
        if not coins:
            return 0
        dp = [[0]*(amount+1) for _ in range(len(coins))]
        for j in range(amount+1):
            if j%coins[0]==0:
                dp[0][j] = 1
        for i in range(1, len(coins)):
            dp[i][0] = 1
            for j in range(1,amount+1):
                if j>=coins[i]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
# @lc code=end

