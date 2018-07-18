# !usr/bin/python
# -*- coding:utf-8 -*-

def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 用三个变量来记录最大的三个数
    max1 = max2 = max3 = None
    for num in nums:
        if num > max1:
            max2,max3 = max1, max2        # 1 ,2交换到2和3位置去
            max1 = num
        elif num > max2 and num < max1:
            max2,max3 = num,max2
        elif num > max3 and num < max2:
            max3 = num
    return max1 if max3 == None else max3

def main():
    nums = [2,3,0,4,4,0]
    print(thirdMax(nums))

if __name__ == '__main__':
    main()     