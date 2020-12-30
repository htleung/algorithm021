#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if matrix[i][n-1] == target:
                return True
            if matrix[i][n-1] > target:
                break
        left = 0
        right = n-1
        while left<=right:
            mid = (left+right)//2
            if matrix[i][mid]==target:
                return True
            elif matrix[i][mid]>target:
                right = mid - 1
            elif matrix[i][mid]<target:
                left = mid + 1
        return False
# @lc code=end

