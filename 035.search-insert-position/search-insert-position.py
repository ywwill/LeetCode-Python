# !usr/bin/python
# -*- coding:utf-8 -*-

def searchInsert(nums, target):
    left = 0
    right = len(nums) -1
    while left <= right:
        mid = (right - left) / 2 + left
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left



def main():
    nums = [1,3,5,6,7]
    print(searchInsert(nums, 4))


if __name__ == '__main__':
    main()