#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0,1)
        nums.insert(len(nums),1)
        dp = [[0]*len(nums) for _ in range(len(nums))]

        def range_best(i,j):
            m = 0
            for k in range(i+1,j):
                left = dp[i][k]
                right = dp[k][j]
                a = left + nums[i]*nums[k]*nums[j] + right
                if a>m:
                    m = a
            dp[i][j] = m

        for n in range(2, len(nums)):
            for i in range(0,len(nums)-n):
                range_best(i,i+n)
        return dp[0][len(nums)-1]
# @lc code=end

