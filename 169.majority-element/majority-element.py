# !usr/bin/python
# -*- coding:utf-8 -*-

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 由于一定存在，所以只需排序，然后取length/2的元素
    return sorted(nums)[len(nums) / 2]


def main():
    nums = [1, 1, 2, 3, 5]
    print(majorityElement(nums))

if __name__ == '__main__':
    main()
        