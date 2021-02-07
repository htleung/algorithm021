#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        #dp:已知dp[n]，则dp[n+1]是找到n最低位的0的位置,dp[n+1]=dp[n]-p+1
        res = [0]
        for n in range(num):
            one = (~n) & (-(~n))
            pos = bin(one-1).count("1")
            res.append(res[-1]-pos+1)
        return res
# @lc code=end

