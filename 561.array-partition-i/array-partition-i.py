# !usr/bin/python
# -*- coding:utf-8 -*-

def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 结果便是排序后第1，3，5，...2n-1数的和
    return sum(sorted(nums)[::2])

def main():
    nums = [1,4,3,2]
    print(arrayPairSum(nums))

if __name__ == '__main__':
    main()     
