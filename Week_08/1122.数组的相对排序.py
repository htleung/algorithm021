#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        #解法一：利用内置sorted函数的key自定义排序准则
        #return sorted(arr1, key=lambda x:(0,arr2.index(x)) if x in arr2 else (1, x))
        #解法二：桶排序
        temp = [0]*(max(arr1)+1)
        res = []
        for x in arr1:
            temp[x]+=1
        for t in arr2:
            if temp[t]>0:
                res.extend([t]*temp[t])
                temp[t] = 0
        for i in range(max(arr1)+1):
            if temp[i]>0:
                res.extend([i]*temp[i])
        return res
# @lc code=end

