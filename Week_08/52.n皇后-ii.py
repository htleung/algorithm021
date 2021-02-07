#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
    #用set记录已占位置的DFS
    #     if n<1:
    #         return []
    #     self.result = []
    #     self.cols = set()
    #     self.pie = set()
    #     self.na = set()
    #     self.DFS(n,0,[])
    #     self.generate_result(n)
    #     return len(self.result)
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

    #用bit记录已占位置的DFS
        if n<1:
            return []
        self.count = 0
        self.DFS(n, 0, 0, 0, 0)
        return self.count
    def DFS(self, n, row, cols, pie, na):
        #cols，pie, na: 有N个二进制位的整数，记录cols，pie和na在当前第row行会与已放置皇后产生冲突的列位置
        if row >= n:
            self.count += 1
            return
        bits = (~(cols|pie|na)) & ((1<<n)-1)
        #(cols|pie|na):列撇捺都没有冲突的位置为0，取反则为1，(1<<n)-1：n个低位置为1
        # 两者按位与，已经有皇后占据的列为0，可以放置的列为1
        while bits: #当bits不为0时，即还有可以尝试放置皇后的位置，与解法一中的for col in range(n)一样，遍历所有可以放置的位置
            p = bits & -bits #取得bits最低位的1
            bits = bits & (bits - 1) #最低位的1置为0
            self.DFS(n, row+1, cols|p, (pie|p)<<1, (na|p)>>1) #想象一下下移一行后pie和na的位移
            #不需要回复cols, pie, na，因为是整数





# @lc code=end

