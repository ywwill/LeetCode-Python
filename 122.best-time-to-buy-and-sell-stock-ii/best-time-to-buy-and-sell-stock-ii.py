# !usr/bin/python
# -*- coding:utf-8 -*-

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # 只要后面比前面大就加上
    return sum(max(prices[i+1]-prices[i],0) for i in range(len(prices)-1))

def main():
    nums = [7, 1, 5, 3, 6, 4]
    print(maxProfit(nums))

if __name__ == '__main__':
    main()