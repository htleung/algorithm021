#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        temp = ""
        i = 0
        while i<len(s) and s[i]==" ":
            i += 1
        flag = 1
        if i<len(s) and s[i] in ['-','+']:
            if s[i] == '-':
                flag = -1
                i += 1
            elif s[i] == '+':
                i += 1
        while i<len(s) and s[i]=='0':
            i += 1
        nums = ['1','2','3','4','5','6','7','8','9','0']
        while i<len(s) and s[i] in nums:
            temp += s[i]
            i += 1
        res = 0
        if len(temp):
            res = int(temp)*flag
        else:
            return 0
        if res<-2**31:
            return -2**31
        elif res>2**31-1:
            return 2**31-1
        return res
# @lc code=end

