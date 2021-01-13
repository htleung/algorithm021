#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def sub_rob(node):
            if not node:
                return {'rob':0, 'not_rob':0}
            left = sub_rob(node.left)
            right = sub_rob(node.right)
            rob = node.val + left['not_rob'] + right['not_rob']
            not_rob = max(left['rob'], left['not_rob']) + max(right['rob'], right['not_rob'])
            return {'rob':rob, 'not_rob':not_rob}
        res = sub_rob(root)
        return max(res['rob'], res['not_rob'])
        
# @lc code=end

