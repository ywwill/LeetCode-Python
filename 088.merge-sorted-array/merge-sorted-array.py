# !usr/bin/python
# -*- coding:utf-8 -*-

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtyp
    """
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m = m - 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n = n - 1
    if n > 0:
        nums1[:n] = nums2[:n]
        # 在nums2元素多余nums1时，nums2剩余一个元素，将nums2的第一个元素赋值到nums1的第一个位置


def merge2(nums1, nums2):
    ans = []
    i, j = 0, 0
    n , m = len(nums1), len(nums2)
    while i < n and j < m:
        if nums1[i] < nums2[j]:
            ans.append(nums1[i])
            i += 1
        else:
            ans.append(nums2[j])
            j += 1
    while i < n:
        ans.append(nums1[i])
        i += 1
    while j < m:
        ans.append(nums2[j])
        j += 1
    return ans


def main():
    nums1 = [2,4,6,8]
    nums2 = [1,3,5,7]
    print(merge2(nums1, nums2))

if __name__ == '__main__':
    main()