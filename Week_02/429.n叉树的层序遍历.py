#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        d = {}
        queue = [(0, root)]
        level = 0
        while len(queue)>0:
            ind, node = queue.pop(0)
            if ind in d:
                d[ind].append(node.val)
            else:
                d[ind] = [node.val]
            if node.children:
                level  = ind + 1
                for ch in node.children:
                    queue.append((ind+1, ch))
        res = []
        for i in range(level+1):
            res.append(d[i])
        return res
        
# @lc code=end

