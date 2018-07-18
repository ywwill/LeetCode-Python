# !usr/bin/python
# -*- coding:utf-8 -*-

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    # python切片操作
    n = len(nums)
    nums[:] = nums[n-k:] + nums[:n-k]

def main():
    nums = [0, 1, 3, 5, 6, 8]
    rotate(nums, 3)
    print(nums)

if __name__ == '__main__':
    main()
           
            
        