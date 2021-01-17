#
# @lc app=leetcode.cn id=403 lang=python3
#
# [403] 青蛙过河
#

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        d = {}
        for s in stones:
            d[s] = set()
        d[stones[0]].add(0)
        for i in range(len(stones)):
            for k in d[stones[i]]:
                if k-1>0 and stones[i]+k-1 in stones:
                    d[stones[i]+k-1].add(k-1)
                if stones[i]+k in stones:
                    d[stones[i]+k].add(k)
                if stones[i]+k+1 in stones:
                    d[stones[i]+k+1].add(k+1)
        return len(d[stones[-1]])>0
# @lc code=end

