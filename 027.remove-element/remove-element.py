# !usr/bin/python
# -*- coding:utf-8 -*-

def removeElement(nums, val):
    index = -1
    for i in xrange(0, len(nums)):
        if nums[i] != val:
            index += 1
            nums[index] = nums[i]
    return index + 1


def main():
    nums = [3,2,2,3]
    removeElement(nums, 3)
    print(nums)


if __name__ == '__main__':
    main()