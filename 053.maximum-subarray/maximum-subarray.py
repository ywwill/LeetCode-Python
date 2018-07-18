# !usr/bin/python
# -*- coding:utf-8 -*-

def maxSubArray(nums):
    currentSum = maxSum = nums[0]
    for i in xrange(1, len(nums)):
        currentSum = max(nums[i], currentSum + nums[i])
        maxSum = max(maxSum, currentSum)
    return maxSum

def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))

if __name__ == '__main__':
    main()