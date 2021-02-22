#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n<3:
            return []
        nums.sort()
        ans = []
        for i in range(n):
            if nums[i]>0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j<k:
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j<k and nums[j] == nums[j+1]:
                        j += 1
                    while j<k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    while j<k and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    while j<k and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
        return ans
# @lc code=end

