#
# @lc app=leetcode.cn id=363 lang=python3
#
# [363] 矩形区域不超过 K 的最大数值和
#

# @lc code=start
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        #遍历左右边界
        #对于某一个左右边界，计算边界范围内矩阵的不大于k的最大矩阵和
        #   1.计算左右边界内每一行的行和,记录到数组s[0:row]
        #   2.从0开始累加每一行的和，记录到数组arr[i],表示目前左右边界内从0号到i行的累加和
        #   3.当累加到超过k时，用二分法找到curr_sum-k的位置loc，也即区域和中最接近k的位置，
        #   更新当前最大和curr_max=max(curr_sum-arr[loc], curr_max)
        import bisect
        row = len(matrix)
        col = len(matrix[0])
        cur_max = -float('inf')
        for left in range(col):
            s = [0]*row
            for right in range(left, col):
                for j in range(row):
                    s[j] += matrix[j][right]
                arr = [0]
                cur_sum = 0
                for si in s:
                    cur_sum += si
                    loc = bisect.bisect_left(arr, cur_sum-k)
                    if loc<len(arr):
                        cur_max = max(cur_max, cur_sum-arr[loc])
                    bisect.insort(arr, cur_sum)
        return cur_max
# @lc code=end

