#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def isChild(node, n):
            diff = 0
            for i in range(len(node)):
                if node[i] != n[i]:
                    diff += 1
                if diff>1:
                    return False
            return True
        if end not in bank:
            return -1
        f_queue = []
        b_queue = []
        f_queue.append(start)
        b_queue.append(end)
        level_f = 0
        level_b = 0
        visited_f = [False]*len(bank)
        visited_b = [False]*len(bank)
        while f_queue and b_queue:
            size_f = len(f_queue)
            size_b = len(b_queue)
            level_f += 1
            for _ in range(size_f):
                node = f_queue.pop(0)
                for i, n in enumerate(bank):
                    if not visited_f[i]:
                        if isChild(node, n):
                            if n==end:
                                return level_f
                            visited_f[i] = True
                            f_queue.append(n)
                            if visited_b[i]:
                                return level_f + level_b
            level_b += 1
            for _ in range(size_b):
                node = b_queue.pop(0)
                for i,n in enumerate(bank):
                    if not visited_b[i]:
                        if isChild(node,n):
                            visited_b[i] = True
                            b_queue.append(n)
                            if visited_f[i]:
                                return level_f + level_b
        return -1
# @lc code=end

