# !usr/bin/python
# -*- coding:utf-8 -*-

def isHappy1(n):
    """
    :type n: int
    :rtype: bool
    """
    c = set()
    while not n in c:
        c.add(n)
        n = sum([pow(int(x),2) for x in str(n)])
    return n == 1

def isHappy2(n):
    c = set()
    while not n in c:
        c.add(n)
        result = 0
        for x in str(n):
            result += pow(int(x),2)
        print(result) #打印每次计算的结果
        n = result
    return n == 1

def main():
    print(isHappy2(12))

if __name__ == '__main__':
    main()