#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""
        k = len(s)
        dp = [[False]*k for _ in range(k)]
        ans = ""
        for l in range(k):
            for i in range(k):
                j = i+l #从i开始，长为l+1的子串是否为回文串
                if j>=len(s):
                    break
                if l==0:
                    dp[i][j] = True
                elif l==1:
                    dp[i][j] = (s[i]==s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and (s[i]==s[j]))
                if dp[i][j] and l+1>len(ans):
                    ans = s[i:j+1]
        return ans
# @lc code=end

