#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            left1 = res[-1][0]
            right1 = res[-1][1]
            left2 = intervals[i][0]
            right2 = intervals[i][1]
            if left2>right1:
                res.append(intervals[i])
            else:
                res[-1] = [left1, max(right1, right2)]
        return res
# @lc code=end

