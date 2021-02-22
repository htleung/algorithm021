#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        right = left = 0
        while right < n:
            if nums[right]!=0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
            right += 1
# @lc code=end

