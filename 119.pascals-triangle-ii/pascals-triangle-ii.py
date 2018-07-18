# !usr/bin/python
# -*- coding:utf-8 -*-

def generate(rowIndex):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    res = [1]
    for i in range(1, rowIndex + 1):
        res = list(map(lambda x, y: x + y, res + [0], [0] + res))
    return res

def main():
    print(generate(3))

if __name__ == '__main__':
    main()
        