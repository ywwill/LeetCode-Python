# !usr/bin/python
# -*- coding:utf-8 -*-

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    dict1 = {}
    dict2 = {}

    for i in s:
        dict1[i] = dict1.get(i,0) + 1 # 每个字符出现的次数
    for i in t:
        dict2[i] = dict2.get(i,0) + 1
    return dict1 == dict2

def main():
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s,t))

if __name__ == '__main__':
    main()