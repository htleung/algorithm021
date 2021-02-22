#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        i = 0
        j = 0
        while i<len(s) and j<len(t):
            if s[i] not in ds and t[j] not in dt:
                ds[s[i]] = t[j]
                dt[t[j]] = s[i]
            else:
                if (s[i] in ds and ds[s[i]] != t[j]) or (t[j] in dt and dt[t[j]]!=s[i]):
                    return False
            i += 1
            j += 1
        return True
# @lc code=end

