# !usr/bin/python
# -*- coding:utf-8 -*-

def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    res = ''
    while n:
        res = chr((n-1) % 26 + ord('A')) + res
        n = (n - 1) / 26
    return res

def main():
    n = 28
    print(convertToTitle(n))

if __name__ == '__main__':
    main()