# !usr/bin/python
# -*- coding:utf-8 -*-

def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cnt = 0 # 计数
    ans = 0 # 结果
    for num in nums:
        if num == 1:
            cnt += 1
            ans = max(ans,cnt)
        else:
            cnt = 0
    return ans

def main():
    nums = [0,1,0,0,1,1,1,0]
    print(findMaxConsecutiveOnes(nums))

if __name__ == '__main__':
    main()     