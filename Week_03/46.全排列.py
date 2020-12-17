#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, temp):
            if not nums:
                res.append(temp[:])
                return
            for i in range(len(nums)):
                temp.append(nums[i])
                backtrack(nums[:i]+nums[i+1:], temp)
                temp.pop()
        backtrack(nums, [])
        return res
# @lc code=end

