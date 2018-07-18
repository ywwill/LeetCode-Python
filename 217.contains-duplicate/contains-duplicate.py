# !usr/bin/python
# -*- coding:utf-8 -*-
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    for i in range(0, len(nums) - 1):
        if nums[i] == nums[i+1]:
            return True
    return False

def containsDuplicate2(nums):
    res = dict()
    for i, num in enumerate(nums):
        if num in res:
            return [res[num], i]
        res[num] = i

def main():
    nums = [0, 1, 3, 5, 6, 1]
    print(containsDuplicate2(nums))

if __name__ == '__main__':
    main()
        


