#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        sum = 0
        max_left = [0]*len(height)
        max_right = [0]*len(height)
        for i in range(1, len(height)-1):
            max_left[i] = max(max_left[i-1], height[i-1])
        for j in range(len(height)-2, 0, -1):
            max_right[j] = max(max_right[j+1], height[j+1])
        for k in range(1, len(height)-1):
            if min(max_left[k], max_right[k])>height[k]:
                sum += min(max_left[k], max_right[k]) - height[k]
        return sum
# @lc code=end

