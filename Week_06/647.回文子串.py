#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        count = 0
        for j in range(n):
            for i in range(j+1):
                if len(s[i:j+1])==1:
                    dp[i][j]=True
                    count += 1
                elif len(s[i:j+1])==2:
                    if s[i]==s[j]:
                        dp[i][j] = True
                        count +=1
                else:
                    if s[i]==s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                        count += 1
        return count
        
# @lc code=end

