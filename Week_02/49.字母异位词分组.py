#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            count = [0]*26
            for ch in s:
                count[ord(ch)-ord('a')] += 1
            if tuple(count) in d:
                d[tuple(count)].append(s)
            else:
                d[tuple(count)] = [s]
        res = []
        for key in d:
            res.append(d[key])
        return res
# @lc code=end

