# !usr/bin/python
# -*- coding:utf-8 -*-

def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    dic = dict()

    for str in s:
        dic[str] = dic.get(str, 0) + 1
    for str in t:
        if str in dic:   #随机添加的字母在s和t中都有
            dic[str] = dic[str] - 1
            if dic[str] == 0:
                del dic[str]
        else:
            return str  #随机添加的字母不在s中


def main():
    s = 'abcd'
    t = 'bcade'
    r = 'aabcd'

    print(findTheDifference(s,t))
    print(findTheDifference(s,r))

if __name__ == '__main__':
    main()