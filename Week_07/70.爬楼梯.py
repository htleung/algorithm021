#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        def sub_climb(m):
            if m==1:
                return 1
            if m==2:
                return 2
            return sub_climb(m-1) + sub_climb(m-2)
        return sub_climb(n)
# @lc code=end

