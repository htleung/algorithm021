#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def lcp(start, end):
            if start == end:
                return strs[start]
            mid = (start+end)//2
            leftlcp, rightlcp = lcp(start, mid), lcp(mid+1, end)
            minlen = min(len(leftlcp), len(rightlcp))
            for i in range(minlen):
                if leftlcp[i]!=rightlcp[i]:
                    return leftlcp[:i]
            return leftlcp[:minlen]
        if not strs:
            return ""
        return lcp(0,len(strs)-1)
# @lc code=end

