#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nums = set([1,2,3,4,5,6,7,8,9])
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]
        blanks = []
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    num = int(board[i][j])
                    box_index = (i//3)*3 + j//3
                    rows[i].add(num)
                    cols[j].add(num)
                    boxs[box_index].add(num)
                else:
                    blanks.append((i,j))
        def DFS(n):
            if n==len(blanks):
                return True
            i, j = blanks[n]
            box_index = (i//3)*3 + j//3
            rest = nums - rows[i] - cols[j] - boxs[box_index]
            if not rest:
                return False
            for r in rest:
                board[i][j] = str(r)
                rows[i].add(r)
                cols[j].add(r)
                boxs[box_index].add(r)
                if DFS(n+1):
                    return True
                rows[i].remove(r)
                cols[j].remove(r)
                boxs[box_index].remove(r)
                board[i][j] = '.'
        DFS(0)
# @lc code=end

