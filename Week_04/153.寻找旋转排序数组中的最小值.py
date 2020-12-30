#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        left = 0
        right = len(nums)-1
        if nums[right]>nums[left]:
            return nums[0]
        while left <= right:
            mid = (left+right)//2
            if mid>0 and nums[mid]<nums[mid-1]:
                return nums[mid]
            if mid<len(nums)-1 and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid]>=nums[0]:
                left = mid+1
            elif nums[mid]<nums[0]:
                right = mid-1
# @lc code=end

