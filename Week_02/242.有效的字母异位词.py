#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==0 or len(t)==0:
            return True
        d = {}
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        for ch in t:
            if ch in d:
                d[ch] -= 1
            else:
                return False
        for key in d:
            if d[key]!=0:
                return False
        return True
# @lc code=end

