#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        def reverse(s):
            slist = list(s)
            i = 0
            j = len(slist)-1
            while i<j:
                slist[i], slist[j] = slist[j], slist[i]
                i += 1
                j -= 1
            return ''.join(slist)
        temp = ""
        for ch in S:
            if ch.isalpha():
                temp += ch
        temp = reverse(temp)
        res = ""
        i = 0
        j = 0
        while i<len(S):
            if S[i].isalpha():
                res += temp[j]
                i += 1
                j += 1
            else:
                res += S[i]
                i += 1
        return res
        
# @lc code=end

