# !usr/bin/python
# -*- coding:utf-8 -*-

# 数组元素个数跟元素范围是一样的，所以可以把出现过的元素对应下标位置的
# 数字变成负数，最后把所有正数对应的下标拿出来，就是缺失的数字

def findDisappearedNumbers(nums):
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = -abs(nums[index])

    return [i + 1 for i in range(len(nums)) if nums[i] > 0]

def main():
    nums = [1,1,2,3]
    print(findDisappearedNumbers(nums))

if __name__ == '__main__':
    main()     