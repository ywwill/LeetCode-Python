# !usr/bin/python
# -*- coding:utf-8 -*-

# 第一种方法：将数字的逆序和原来的数字进行比较

def reverse1(x):
    z = x
    y = 0
    while x > 0:
        y = y * 10 + x % 10
        x = x / 10
    return z == y

# 第二种方法，只需要逆序后面一半数字

def reverse2(x):
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    half = 0
    while x > half:
        half = half * 10 + x % 10
        x = x / 10
    return half == x or half / 10 == x

def main():
    print(reverse1(12321))
    print(reverse2(12321))

if __name__ == '__main__':
    main()