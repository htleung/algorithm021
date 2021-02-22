#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or len(s)<len(p):
            return []
        def check():
            for key in d:
                if key not in window or window[key] != d[key]:
                    return False
            return True
        d = {}
        for ch in p:
            if ch not in d:
                d[ch] =1
            else:
                d[ch] += 1
        window = {}
        res = []
        k = len(p)
        for j in range(k):
            if s[j] in window:
                window[s[j]] += 1
            else:
                window[s[j]] = 1
        if check():
            res.append(0)
        for i in range(1, len(s)):
            if i+k>len(s):
                break
            window[s[i-1]] -= 1
            if s[i+k-1] in window:
                window[s[i+k-1]] += 1
            else:
                window[s[i+k-1]] = 1
            if check():
                res.append(i)
        return res
            
# @lc code=end

