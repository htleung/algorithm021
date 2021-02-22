#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = dict()
        for ch in stones:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        res = 0
        for ch in jewels:
            res += d.get(ch, 0)
        return res
# @lc code=end

