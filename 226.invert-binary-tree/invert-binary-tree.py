# Definition for a binary tree node.

# !usr/bin/python
# -*- coding:utf-8 -*-

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left,root.right = invertTree(root.right),invertTree(root.left)
        return root
