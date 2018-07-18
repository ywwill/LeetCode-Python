# !usr/bin/python
# -*- coding:utf-8 -*-

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    curSum=maxSum=0
    for i in range(1,len(prices)):
        curSum=max(0,curSum+prices[i]-prices[i-1])
        maxSum = max(curSum, maxSum)
    return maxSum

def main():
    nums = [7, 1, 5, 3, 6, 4]
    print(maxProfit(nums))

if __name__ == '__main__':
    main()
        