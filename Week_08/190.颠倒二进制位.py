#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        power = 31 #32位无符号整数
        res = 0
        while n:
            bit = n&1 #每次取出最低位
            res += (bit<<power) #往左移
            power -= 1
            n=n >> 1 #右移一位，下次取出的是下一个位
        return res
# @lc code=end

