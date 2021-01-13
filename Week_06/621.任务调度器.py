#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        maxNum = 0
        maxExe = 0
        for t in tasks:
            if t in d:
                d[t] += 1
            else:
                d[t] = 1
        for key in d:
            if d[key]>maxExe:
                maxExe = d[key]
        for key in d:
            if d[key]==maxExe:
                maxNum+=1
        return max((maxExe-1)*(n+1)+maxNum, len(tasks))
# @lc code=end

