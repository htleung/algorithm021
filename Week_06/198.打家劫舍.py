#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        pre = nums[0]
        cur = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            pre, cur = cur, max(cur, pre+nums[i])
        return cur

# @lc code=end

