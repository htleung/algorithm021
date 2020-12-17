#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = list()
        def backtrack(temp, index):
            if len(temp)==k:
                ans.append(temp[:])
                return
            for i in range(index, n+1):
                temp.append(i)
                backtrack(temp, i+1)
                temp.pop()
        backtrack([], 1)
        return ans

# @lc code=end

