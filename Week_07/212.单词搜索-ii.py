#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []
        trie = {}
        end_of_word = '#'
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node[end_of_word] = True
        def dfs(i, j, node, prefix, visited):
            if end_of_word in node:
                res.add(prefix)
            for dx, dy in ((1,0),(0,1),(-1,0),(0,-1)):
                temp_i = i+dx
                temp_j = j+dy
                if -1<temp_i<m and -1<temp_j<n and board[temp_i][temp_j] in node and (temp_i,temp_j) not in visited:
                    visited.append((temp_i, temp_j))
                    dfs(temp_i, temp_j, node[board[temp_i][temp_j]], prefix+board[temp_i][temp_j], visited)
                    visited.pop()
        res = set()
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie[board[i][j]], board[i][j], [(i,j)])
        return list(res)
# @lc code=end

