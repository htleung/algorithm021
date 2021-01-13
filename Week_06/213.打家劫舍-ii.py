#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def sub_rob(nums):
            if not nums:
                return 0
            if len(nums)==1:
                return nums[0]
            pre = nums[0]
            cur = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                pre, cur = cur, max(cur, pre+nums[i])
            return cur
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        return max(sub_rob(nums[1:]), sub_rob(nums[:-1]))
# @lc code=end

