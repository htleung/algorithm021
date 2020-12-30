#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = nums[0]
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                if target >= start:
                    right = mid - 1
                elif target < start:
                    if nums[mid]>=start:
                        left = mid + 1
                    else:
                        right = mid -1 
            elif nums[mid]<target:
                if target >= start:
                    if nums[mid]>=start:
                        left = mid + 1
                    else:
                        right = mid - 1
                elif target < start:
                    left = mid + 1
        return -1
    # @lc code=end

