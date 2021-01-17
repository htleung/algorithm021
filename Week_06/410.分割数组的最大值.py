#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        #“使...最大值尽可能小”，二分查找中的找边界问题
        #要使用二分查找，要先确定第一查找范围，第二查找对象有序
        #确定范围：子数组的最小值必定>=数组中的最大值，最大值就是整个数组的和
        def check(x): #check能不能在分成m组的情况下，使得这些子数组的数组和都不大于x
            total, count = 0, 1
            for num in nums:
                if total + num > x: #当前的累计和大于x时，说明要再分一个子数组
                    count += 1
                    total = num
                else:
                    total += num
            return count <= m
        left = max(nums)
        right = sum(nums)
        while left<right:
            mid = (left+right) // 2
            if check(mid):
                right = mid
            else:
                left = mid+1
        return left

    # @lc code=end

