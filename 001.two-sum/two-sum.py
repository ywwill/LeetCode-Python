# !usr/bin/python
# -*- coding:utf-8 -*-

def twoSum(nums, target):
    res = dict()
    for i, num in enumerate(nums):
        if target - num in res:
            return [res[target-num], i]
        res[num] = i

def main():
    nums = [1,2,3,4,5,6,8,9]
    print(twoSum(nums, 15))

if __name__ == '__main__':
    main()