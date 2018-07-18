# !usr/bin/python
# -*- coding:utf-8 -*-

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 0: return []
    res = [[1]]
    for i in range(1,numRows):
        res.append(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))
    return res

def main():
    print(generate(5))

if __name__ == '__main__':
    main()