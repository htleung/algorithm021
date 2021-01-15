#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for c in coins:
                if i<c:
                    continue
                dp[i] = min(dp[i], dp[i-c]+1)
        if dp[-1]==float('inf'):
            return -1
        return dp[-1]
# @lc code=end

