#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def ischild(parent, child): #判断是否为子节点
            diff = 0
            for i in range(len(parent)):
                if parent[i]!=child[i]:
                    diff += 1
                if diff > 1:
                    return False
            return True
        if endWord not in wordList: #先判断特例
            return 0
        q_b = [] #从begin开始找的队列
        q_e = [] #从end开始找的队列
        q_b.append(beginWord)
        q_e.append(endWord)
        visited_b = [False]*len(wordList) #记录从begin开始访问过的节点
        visited_e = [False]*len(wordList) #记录从end开始访问过的节点
        level_b = 0
        level_e = 0
        while q_b and q_e:
            size_b = len(q_b)
            size_e = len(q_e)
            level_b += 1
            for _ in range(size_b): #从begin开始查找
                node = q_b.pop(0)
                for i, w in enumerate(wordList): #遍历所有单词，看是否为当前节点的子节点
                    if not visited_b[i]:
                        if ischild(node, w):
                            if w==endWord: #如果是结束节点，可以直接返回从begin开始已经走过的路径长度
                                return level_b+1
                            visited_b[i] = True
                            q_b.append(w)
                            if visited_e[i]:#如果从结束节点开始也能走到这个节点，说明这条路是通的，返回两边路径的长度之和
                                return level_b + level_e + 1
            level_e += 1
            for _ in range(size_e):
                node = q_e.pop(0)
                for i, w in enumerate(wordList):
                    if not visited_e[i]:
                        if ischild(node, w):
                            visited_e[i] = True
                            q_e.append(w)
                            if visited_b[i]:
                                return level_b + level_e + 1
        return 0
# @lc code=end

