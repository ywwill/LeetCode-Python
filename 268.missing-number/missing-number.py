# !usr/bin/python
# -*- coding:utf-8 -*-

def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    return (n*(n+1))/2 - sum(nums)
    

def main():
    nums = [0,1,2,3,4,6]
    print(missingNumber(nums))

if __name__ == '__main__':
    main()
