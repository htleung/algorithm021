#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        def reverse(start, end):
            i = start
            j = end
            while i<j:
                s[i], s[j] = s[j],s[i]
                i += 1
                j -= 1
        index = 0
        while index<len(s):
            start = index
            end = min(len(s)-1, start+k-1)
            reverse(start, end)
            index += 2*k 
        return ''.join(s)
        
# @lc code=end

