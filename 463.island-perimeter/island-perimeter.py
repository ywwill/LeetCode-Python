# !usr/bin/python
# -*- coding:utf-8 -*-


def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    '''
    统计neighbor时，为了避免重复，只循环每一个元素的上方和左方元素是否为1
    统计岸边的数量，num = 1的个数 * 4 - neighbor * 2
    '''
    num = 0
    neighbor = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                num = num + 1
                if i > 0 and grid[i-1][j] == 1: # 上边
                    neighbor = neighbor + 1
                
                if j > 0 and grid[i][j-1] == 1: # 左边
                    neighbor = neighbor + 1
    return num * 4 - neighbor * 2

def main():
    grid = [[0,1,0,0],[1,1,1,1],[0,1,0,0],[1,1,0,0]]
    print(islandPerimeter(grid))

if __name__ == '__main__':
    main()