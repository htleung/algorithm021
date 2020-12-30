#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        j = 0
        count = 0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                j+=1
                i+=1
                count+=1
            else:
                j+=1
        return count
        
# @lc code=end

