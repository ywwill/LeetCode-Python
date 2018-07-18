# !usr/bin/python
# -*- coding:utf-8 -*-

def matrixReshape(nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    if len(nums) * len(nums[0]) != r * c:
        return nums
    else:
        # 展开
        onerow = [nums[i][j] for i in range(len(nums)) for j in range(len(nums[0]))]
        # 区间取值
        return [onerow[t * c:(t + 1) * c] for t in range(r)]

def main():
    nums = [[1,2],[3,4],[5,6],[7,8]]
    print(matrixReshape(nums,2,4))

if __name__ == '__main__':
    main()     
