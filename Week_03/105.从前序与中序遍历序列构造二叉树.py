#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0:
            return None
        if len(preorder)==1:
            return TreeNode(preorder[0])
        #2. process current level
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]
        left_preorder = preorder[1:1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder):]
        #3. drill down
        left = self.buildTree(left_preorder, left_inorder)
        right = self.buildTree(right_preorder, right_inorder)
        root.left = left
        root.right = right
        return root
# @lc code=end

