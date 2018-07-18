# !usr/bin/python
# -*- coding:utf-8 -*-
import collections

def findPairs(nums, k):
    if k>0:
        # 返回两个集合的交集
        return len(set(nums) & set(n+k for n in nums))
    elif k==0:
        # 统计出现次数>1的
        return sum(v>1 for v in collections.Counter(nums).values())
    else:
        return 0

def main():
    nums = [3,5,1,4,1,5]
    print(findPairs(nums,0))

if __name__ == '__main__':
    main()     