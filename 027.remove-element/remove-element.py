# !usr/bin/python
# -*- coding:utf-8 -*-

def removeElement(nums, val):
    index = -1
    for i in xrange(0, len(nums)):
        if nums[i] != val:
            index += 1
    return index + 1


def main():
    nums = [3,2,2,3]
    print(removeElement(nums, 3))


if __name__ == '__main__':
    main()