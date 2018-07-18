# !usr/bin/python
# -*- coding:utf-8 -*-

def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    dic = dict()
    for index,value in enumerate(nums):
        if value in dic and index - dic[value] <= k:
            print(dic[value], index)
            return True
        dic[value] = index
    return False

def main():
    nums = [-1,0,2,-1]
    containsNearbyDuplicate(nums, 3)

if __name__ == '__main__':
    main()
        
            