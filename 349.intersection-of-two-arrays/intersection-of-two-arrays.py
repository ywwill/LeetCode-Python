# !usr/bin/python
# -*- coding:utf-8 -*-

def intersection1(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    d = {}
    ans = []
    for num in nums1:
        d[num] = d.get(num, 0) + 1
    
    for num in nums2:
        if num in d:
            ans.append(num)
            del d[num] # 存在便删除字典中的元素
    return ans

def intersection2(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    nums1 = set(nums1)
    return [x for x in set(nums2) if x in nums1]

def main():
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(intersection1(nums1, nums2))
    print(intersection2(nums1, nums2))

if __name__ == '__main__':
    main()