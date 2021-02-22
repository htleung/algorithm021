#
# @lc app=leetcode.cn id=709 lang=python3
#
# [709] 转换成小写字母
#

# @lc code=start
class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ''
        for ch in str:
            if 65<=ord(ch)<=90:
                res += chr(ord(ch)+32)
            else:
                res += ch
        return res
# @lc code=end

