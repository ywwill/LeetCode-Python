# !usr/bin/python
# -*- coding:utf-8 -*-

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if (p.val - root.val) * (q.val - root.val) <= 0: # 如果两个节点一个值比节点大，一个比节点小，或者与根结点的值同样大,那么二者的公共节点肯定是根结点
            return root
        if p.val < root.val and q.val < root.val: # 两个节点的值都比根结点小，那么二者的公共节点出现在根结点的左子树中，递归查询
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val: # 两个节点的值都比根结点大，那么二者的公共节点出现在根结点的右子树中，递归查询
            return self.lowestCommonAncestor(root.right, p, q)