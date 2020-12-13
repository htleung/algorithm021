#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        return self.preorder_recur(root, res)

    def preorder_recur(self, root, res):
        if root is not None:
            res.append(root.val)
            for ch in root.children:
                self.preorder_recur(ch, res)
        return res
        
        
# @lc code=end

