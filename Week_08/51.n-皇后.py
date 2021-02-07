#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 用set记录已经占位置的DFS
    #     if n<1:
    #         return []
    #     self.result = []
    #     self.cols = set()
    #     self.pie = set()
    #     self.na = set()
    #     self.DFS(n,0,[])
    #     self.generate_result(n)
    #     return self.result
    # def DFS(self, n, row, state):
    #     if row>=n:
    #         self.result.append(state)
    #     for col in range(n):
    #         if col in self.cols or row+col in self.pie or row-col in self.na:
    #             continue
    #         self.cols.add(col)
    #         self.pie.add(row+col)
    #         self.na.add(row-col)
    #         self.DFS(n,row+1,state+[col])
    #         self.cols.remove(col)
    #         self.pie.remove(row+col)
    #         self.na.remove(row-col)
    # def generate_result(self,n):
    #     for i in range(len(self.result)):
    #         ans = self.result[i]
    #         temp = []
    #         for col in ans:
    #             row = ''
    #             for j in range(col):
    #                 row += '.'
    #             row += 'Q'
    #             for j in range(n-col-1):
    #                 row += '.'
    #             temp.append(row)
    #         self.result[i] = temp
        #用位运算来记录已占位置的递归
        def DFS(n, row, cols, pie, na):
            #cols，diag1, diag2: 有N个二进制位的整数，记录cols，pie和na在当前第row行会与已放置皇后产生冲突的列位置
            if row>=n:
                board = generate_board()
                res.append(board)
            else:
                availableCols = (~(cols|pie|na)) & ((1<<n)-1) 
                #(cols|pie|na):列撇捺都没有冲突的位置为0，取反则为1，(1<<n)-1：n个1，两者按位与，已经有皇后占据的列为0，可以放置的列为1
                while availableCols:
                    position = availableCols & (-availableCols) #取得最低位的1
                    availableCols = availableCols & (availableCols - 1) #将最低位的1清零
                    column = bin(position-1).count("1") #取得position中1的位置
                    queens[row] = column
                    DFS(n, row+1, cols|position, (pie|position)<<1, (na|position)>>1)
        def generate_board():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board
        res = list()
        queens = [-1]*n
        row = ["."]*n
        DFS(n,0,0,0,0)
        return res


# @lc code=end

