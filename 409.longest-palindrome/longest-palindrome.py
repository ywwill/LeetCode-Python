# !usr/bin/python
# -*- coding:utf-8 -*-

import collections

def longestPalindrome1(s):
    """
    :type s: str
    :rtype: int
    """

    '''
    最长的回文数可以由三部分组成：
    1、出现次数为偶数的，总长度增加其出现次数
    2、出现次数为奇数，但是大于1次的，此时总长度增加其出现次数-1次
    3、总长度为偶数时，此时只要有出现次数为奇数的元素，总长度再加1
    '''     
    
    t = collections.Counter(s)
    ans = 0

    for x in t:
        if t[x] % 2 == 0:
            ans += t[x]
        if t[x] % 2 == 1 and t[x] > 1:
            ans += t[x] - 1
        if ans % 2 == 0 and t[x] % 2 == 1: # 中间的字母还没添加
            ans += 1
    return ans

def longestPalindrome2(s):
    """
    :type s: str
    :rtype: int
    """
    ans = 0
    for v in collections.Counter(s).itervalues(): # 'aaaaa',  'aaaa' 合适, 所以 5 / 2 * 2 = 4，只要是出现次数大于1的都可以判断出
        ans += v / 2 * 2
        if ans % 2 == 0 and v % 2 == 1: # 中间的字母还没添加
            ans += 1
    return ans


def main():
    s = 'aaabbccddf'
    print(longestPalindrome1(s))
    print(longestPalindrome2(s))

if __name__ == '__main__':
    main()