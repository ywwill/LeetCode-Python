# !usr/bin/python
# -*- coding:utf-8 -*-

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _,ans = self.sumTree(root)
        return ans

    def sumTree(self,node):
        if not node:
            return 0,0
        left,ans1 = self.sumTree(node.left)
        right,ans2 = self.sumTree(node.right)
        return node.val+left+right,abs(right-left)+ans1+ans2