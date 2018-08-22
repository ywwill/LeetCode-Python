# !usr/bin/python
# -*- coding:utf-8 -*-

def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    lo = 0
    hi = x
    while lo <= hi:
        mid = (hi + lo) / 2
        v = mid * mid
        if v < x:
            lo = mid + 1
        elif v > x:
            hi = mid - 1
        else:
            return mid
    return hi

def main():
    num = 37
    print(mySqrt(num))

if __name__ == '__main__':
    main()