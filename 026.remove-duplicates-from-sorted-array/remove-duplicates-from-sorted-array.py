# !usr/bin/python
# -*- coding:utf-8 -*-

def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        slow = 0
        for i in xrange(1, len(nums)):
            if nums[i] != nums[slow]:
                slow += 1
                nums[slow] = nums[i]
        return slow + 1

def main():
    nums = [1,2,2,2,3] # 排好序的数组
    removeDuplicates(nums)
    print(nums)

if __name__ == '__main__':
    main()