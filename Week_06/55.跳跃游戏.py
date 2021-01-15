#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i+nums[i]>=lastPos:
                lastPos = i
        return lastPos==0
# @lc code=end

