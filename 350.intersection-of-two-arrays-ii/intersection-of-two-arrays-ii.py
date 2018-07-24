# !usr/bin/python
# -*- coding:utf-8 -*-

import collections

def intersect1(nums1, nums2):
    ans = []
    nums1.sort() # 排序
    nums2.sort()

    i = j =  0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            ans.append(nums1[i])
            i += 1
            j +=1
    return ans

def intersect2(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    dic1,dic2 = dict(),dict()
    for num in nums1:
        dic1[num] = dic1.get(num,0) + 1 # 使用字典记录每个元素出现的次数
    for num in nums2:
        dic2[num] = dic2.get(num,0) + 1
    return [x for x in dic2 for _ in range(min(dic1.get(x,0),dic2.get(x,0)))]

def intersect3(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    ans = []
    
    # 使用python内置Counter类型
    c1, c2 = collections.Counter(nums1), collections.Counter(nums2)
    
    for i in c1.keys():
        for _ in range(min([c1[i],c2[i]])):
            ans.append(i)
    return ans

    # 简写 
    # return [i for i in c1.keys() for _ in range(min([c1[i],c2[i]]))]


def main():
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(intersect1(nums1, nums2))
    print(intersect2(nums1, nums2))
    print(intersect3(nums1, nums2))

if __name__ == '__main__':
    main()