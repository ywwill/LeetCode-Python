# !usr/bin/python
# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree: # 创建树
    def __init__(self):
        self.root = None

    def add(self, item):
        node = TreeNode(item)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]

            while True:
                pop_node = q.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def traverse(self):  # 层次遍历
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.val]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.left is not None:
                q.append(pop_node.left)
                res.append(pop_node.left.val)

            if pop_node.right is not None:
                q.append(pop_node.right)
                res.append(pop_node.right.val)
        return res

def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p and q:
        if p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right):
            return True
        else:
            return False
    return p is q

def main():
    t1 = Tree()
    t2 = Tree()
    for i in range(6):
        t1.add(i)
        t2.add(i)

    t2.add(6)

    print(t1.traverse())
    print(t2.traverse())

    print(isSameTree(t1.root, t2.root))

if __name__ == '__main__':
    main()

