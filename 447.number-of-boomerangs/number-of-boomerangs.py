# !usr/bin/python
# -*- coding:utf-8 -*-

def numberOfBoomerangs(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    res = 0
    for p in points:
        cmap = {}
        for q in points:
            dis = (p[0]-q[0]) ** 2 + (p[1]-q[1])**2
            cmap[dis] = cmap.get(dis,0)+1
        for key in cmap:
            res += (cmap[key]) * (cmap[key]-1)
    return res
def main():
    a = [[0,0],[1,0],[2,0]]
    print(numberOfBoomerangs(a))
    
if __name__ == '__main__':
    main()
            