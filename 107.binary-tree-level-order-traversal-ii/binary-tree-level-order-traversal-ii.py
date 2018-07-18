# !usr/bin/python
# -*- coding:utf-8 -*-

# Definition for a binary tree node.

from collections import deque

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

def levelOrderBottom(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    stack = [(root,0)] # 树的根结点入栈
    res = []
    while stack!=[]:
        node,level = stack.pop() # 判断栈是否为空，不为空，则出栈，并输出出栈树结点的值
        if node:
            if len(res) < (level+1):
                res.insert(0,[])
            res[-(level+1)].append(node.val)
            stack.append((node.right,level+1)) # 出栈树结点的右子树入栈
            stack.append((node.left,level+1)) # 出栈树结点的左子树入栈
    return res    

def main():
    t = Tree()
    nums = [3,9,20,None,None,15,7]
    for i in range(len(nums)):
        t.add(nums[i])

    print(t.traverse())

    print('bottom-up level order traversal:',levelOrderBottom(t.root))

if __name__ == '__main__':
    main()