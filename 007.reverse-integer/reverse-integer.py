# !usr/bin/python
# -*- coding:utf-8 -*-

def reverse(x):
    # 判断正负
    sign = x < 0 and -1 or 1
    x = abs(x)
    ans = 0
    while x:
        ans = ans * 10 + x % 10
        x /= 10
    return sign * ans if ans <= 0x7fffffff else 0

def main():
    print(reverse(123456))

if __name__ == '__main__':
    main()