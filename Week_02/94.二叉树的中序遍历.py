#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''迭代
        p = root
        stack = []
        res = []
        while len(stack)>0 or p:
            while p:
                stack.append(p)
                p = p.left
            if len(stack)>0:
                p = stack.pop()
                if p:
                    res.append(p.val)
                p = p.right
        return res
        '''
        '''递归'''
        res = []
        self.inorder(root, res)
        return res
    def inorder(self, root, res):
        if root is None:
            return 
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)
# @lc code=end

