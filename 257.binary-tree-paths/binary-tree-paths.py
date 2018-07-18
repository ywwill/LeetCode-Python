# !usr/bin/python
# -*- coding:utf-8 -*-


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self,root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        paths = []
        if root.left != None:
            paths += [str(root.val) + '->' + t for t in self.binaryTreePaths(root.left)]
        if root.right != None:
            paths += [str(root.val) + '->' + t for t in self.binaryTreePaths(root.right)]
        return paths
