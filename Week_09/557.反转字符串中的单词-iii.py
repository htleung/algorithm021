#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(word):
            w = list(word)
            i = 0
            j = len(w)-1
            while i<j:
                w[i], w[j] = w[j], w[i]
                i += 1
                j -= 1
            return ''.join(w)
        
        slist = s.split()
        for i, word in enumerate(slist):
            slist[i] = reverse(word)
        return ' '.join(slist)
# @lc code=end

