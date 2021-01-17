#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dt, ds = {}, {}
        for ch in t:
            if ch in dt:
                dt[ch] += 1
            else:
                dt[ch] = 1
        left = 0 #窗口左右边界为left和right
        right = 0
        start = 0
        length = len(s)+1 #最终结果为s[start:start+length],因为数组切片是左闭右开，因此这里要+1, 初始化为整个s的长度+1
        valid = 0
        while right<len(s):
            c = s[right] #新加进窗口的字符
            right += 1
            if c in dt:
                if c in ds:
                    ds[c]+=1
                else:
                    ds[c]=1
                if ds[c]==dt[c]: #如果窗口内的c字符个数和t中c字符的个数一样，则有效覆盖字符加1
                    valid += 1
            while valid == len(dt): #窗口满足覆盖所有t中的字符后，开始收缩
                if right - left < length:
                    length = right - left
                    start = left
                c = s[left] #将从窗口退出的字符
                left += 1
                if c in dt:
                    if dt[c] == ds[c]:
                        valid -= 1
                    ds[c] -= 1
        return s[start:start+length] if length != len(s)+1 else ''

# @lc code=end

