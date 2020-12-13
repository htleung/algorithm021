#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.preorder(root, res)
        return res
    def preorder(self, root, res):
        if root is None:
            return
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res) 
# @lc code=end

