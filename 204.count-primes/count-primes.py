# !usr/bin/python
# -*- coding:utf-8 -*-

import math

# 计算小于n的质数数量
def countPrimes(n):
    if n < 3:
        return 0

    res = [True] * n
    res[0] = res[1] = False
    for i in range(2,int(math.sqrt(n)) + 1):
        res[i*i:n:i] = [False] * len(res[i*i:n:i])
    
    for i in range(len(res)):
        if res[i] != 0:
            print(i)

    return sum(res)

def main():
    print('质数数量 -- ',countPrimes(100))

if __name__ == '__main__':
    main()