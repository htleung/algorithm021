#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n<1:
            return []
        self.result = []
        self.cols = set()
        self.pie = set()
        self.na = set()
        self.DFS(n,0,[])
        self.generate_result(n)
        return self.result
    def DFS(self, n, row, state):
        if row>=n:
            self.result.append(state)
        for col in range(n):
            if col in self.cols or row+col in self.pie or row-col in self.na:
                continue
            self.cols.add(col)
            self.pie.add(row+col)
            self.na.add(row-col)
            self.DFS(n,row+1,state+[col])
            self.cols.remove(col)
            self.pie.remove(row+col)
            self.na.remove(row-col)
    def generate_result(self,n):
        for i in range(len(self.result)):
            ans = self.result[i]
            temp = []
            for col in ans:
                row = ''
                for j in range(col):
                    row += '.'
                row += 'Q'
                for j in range(n-col-1):
                    row += '.'
                temp.append(row)
            self.result[i] = temp
# @lc code=end

