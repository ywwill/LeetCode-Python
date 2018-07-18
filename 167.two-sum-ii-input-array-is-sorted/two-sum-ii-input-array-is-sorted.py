# !usr/bin/python
# -*- coding:utf-8 -*-

def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    res = dict()
    for i, num in enumerate(numbers):
        if target - num in res:
            return [res[target-num] + 1, i + 1]
        res[num] = i

def main():
    nums = [0, 1, 3, 5, 6, 8]
    print(twoSum(nums, 7))

if __name__ == '__main__':
    main()
        