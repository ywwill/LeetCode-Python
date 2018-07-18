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

def hasPathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if not root:
        return False
    if root.left == None and root.right == None and root.val == sum:
        return True
    return hasPathSum(root.left, sum - root.val) or hasPathSum(root.right, sum - root.val)

def main():
    t = Tree()
    nums = [5,4,9,11,None,13,4,7,2,None,None,None,1]
    for i in range(len(nums)):
        t.add(nums[i])

    print(t.traverse())

    print('path is exist:',hasPathSum(t.root, 22))

if __name__ == '__main__':
    main()