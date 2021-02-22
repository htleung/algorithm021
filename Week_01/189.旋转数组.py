#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = k % len(nums)
        if m == 0:
            return
        i = 0
        j = len(nums)-1
        self.reverse(nums, i, j)
        i = 0
        j = m-1
        self.reverse(nums, i, j)
        i = m
        j = len(nums)-1
        self.reverse(nums, i, j)
        return
    def reverse(self, nums, i, j):
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    
# @lc code=end

