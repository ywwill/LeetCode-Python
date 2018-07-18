# !usr/bin/python
# -*- coding:utf-8 -*-

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """  
    index = 0
    for num in nums:
        if num != 0:
            nums[index] = num
            index += 1
    for i in range(index, len(nums)):
        nums[i] = 0
    
    return nums

def main():
    nums = [0,1,0,3,4,0]
    print(moveZeroes(nums))

if __name__ == '__main__':
    main()
        
            