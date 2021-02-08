#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #解法一：两个字符串排序后相等
        # if len(s)!=len(t):
        #     return False
        # s = list(s)
        # t = list(t)
        # s.sort()
        # t.sort()
        # for i in range(len(s)):
        #     if s[i]!=t[i]:
        #         return False
        # return True
        #解法二：利用哈希表记录字母个数再对比
        dict1 = {}
        dict2 = {}
        for ch in s:
            if ch not in dict1:
                dict1[ch] = 1
            else:
                dict1[ch] += 1
        for ch in t:
            if ch not in dict2:
                dict2[ch] = 1
            else:
                dict2[ch] += 1
        if len(dict1)!=len(dict2):
            return False
        for key in dict1:
            if key not in dict2 or dict1[key]!=dict2[key]:
                return False
        return True
# @lc code=end

