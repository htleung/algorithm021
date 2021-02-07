#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num!='.':
                    num = int(num)
                    box_index = (i//3)*3 + j//3
                    if num in rows[i] or num in cols[j] or num in boxs[box_index]:
                        return False
                    rows[i].add(num)
                    cols[j].add(num)
                    boxs[box_index].add(num)
        return True
# @lc code=end

