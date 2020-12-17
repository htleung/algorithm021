#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(nums, temp):
            if not nums:
                res.append(temp[:])
                return
            for i in range(len(nums)):
                if i<len(nums)-1 and nums[i]==nums[i+1]:
                    continue
                temp.append(nums[i])
                backtrack(nums[:i]+nums[i+1:], temp)
                temp.pop()
        backtrack(nums, [])
        return res
# @lc code=end

