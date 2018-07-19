# !usr/bin/python
# -*- coding:utf-8 -*-

def isIsomorphic1(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False
    dic1 = dict() # 两个dict分别对应保存两个字符串对应位置的对方字符，只要其中一个不满足条件，则返回错误
    dic2 = dict()
    for i in range(len(s)):
        if (s[i] in dic1 and dic1[s[i]] != t[i]) or (t[i] in dic2 and dic2[t[i]] != s[i]):
            return False
        else:
            dic1[s[i]] = t[i]
            dic2[t[i]] = s[i]
    return True

def isIsomorphic2(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # 使用zip将两个数组对应位置元素相连，再利用set不能有重复元素的特性，判断三者的长度是否相同即可
    return len(set(zip(s,t))) == len(set(s)) == len(set(t))

def main():
    s = 'paper'
    t = 'title'
    print(isIsomorphic2(s,t)) 

if __name__ == '__main__':
    main()