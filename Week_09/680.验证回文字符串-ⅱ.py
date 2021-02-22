#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(left, right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left += 1
                right -=1
            return True
        low = 0
        high = len(s)-1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return check(low+1, high) or check(low, high-1)
        return True
        
# @lc code=end

