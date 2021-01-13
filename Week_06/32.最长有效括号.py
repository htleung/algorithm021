#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s)<2:
            return 0
        n = len(s)
        dp = [0]*n
        if s[0]=='(' and s[1]==')':
            dp[1] = 2
        for i in range(2,n):
            if s[i]=='(':
                continue
            if s[i]==')' and s[i-1]=='(':
                dp[i] = dp[i-2] + 2
            elif s[i]==')' and s[i-1]==')':
                if i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':
                    if i-dp[i-1]-2<0:
                        dp[i] = dp[i-1] + 2
                    else:
                        dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
        return max(dp)
# @lc code=end

