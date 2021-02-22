#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        digits[i] += 1
        while digits[i]>9:
            digits[i] = 0
            i -= 1
            if i>=0:
                digits[i] += 1
            else:
                digits.insert(0, 1)
        return digits
# @lc code=end

