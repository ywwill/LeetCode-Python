# !usr/bin/python
# -*- coding:utf-8 -*-

def singleNumber1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    arr = []
    for num in nums: # 遍历数组是否存在，存在便移除
        if num in arr:
            arr.remove(num)
        else:
            arr.append(num)
    return arr

def singleNumber2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in xrange(1, len(nums)): #将所有的元素异或，出现两次的异或二进制结果为 0000，所有元素异或的结果便是出现一次的
        nums[0] ^= nums[i]
    return nums[0]  

def main():
    nums = [4,1,2,1,2]
    print(singleNumber2(nums))

if __name__ == '__main__':
    main()