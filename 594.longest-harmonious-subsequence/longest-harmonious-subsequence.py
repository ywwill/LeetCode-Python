# !usr/bin/python
# -*- coding:utf-8 -*-

import collections

def findLHS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #for i in nums:
    #    dic[i] = dic.get(i,0) + 1 # 记录nums中元素出现的次数

    dic = dict(collections.Counter(nums)) #计录元素出现的次数
    max = 0 # 找到两个差距为1的元素，这两个元素出现的次数都大于0而且相加出现的次数最大
   
    for i in dic:
        if dic.get(i,0) > 0 and dic.get(i+1,0) > 0 and dic.get(i,0) + dic.get(i+1,0) > max:
            max = dic.get(i,0) + dic.get(i+1,0)
            result = []
            
            for _ in range(dic.get(i,0)):
                result.append(i)

            for _ in range(dic.get(i+1,0)):
                result.append(i+1)
    return max,result

def main():
    nums = [1,3,2,2,5,2,3,7]
    print(findLHS(nums))

if __name__ == '__main__':
    main()