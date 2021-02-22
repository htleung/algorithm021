#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        for i,ch in enumerate(s):
            if d[ch]==1:
                return i
        return -1
# @lc code=end

