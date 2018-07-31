# !usr/bin/python
# -*- coding:utf-8 -*-

def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    res = []
    left = right = 0
    count = len(p)
    dic = dict()
    for i in p:
        dic[i] = dic.get(i,0) + 1 # 记录p中元素出现的次数
    while right < len(s):
        if s[right] in dic.keys():
            if dic[s[right]]>=1:
                count = count - 1
            dic[s[right]] = dic[s[right]]-1
        right = right+1
        if count == 0 :
            res.append(left)
        if right - left == len(p):
            if s[left] in dic.keys():
                if dic[s[left]]>=0:
                    count = count + 1
                dic[s[left]]+=1
            left = left+1
    return res

def main():
    s = 'cbaeb'
    p = 'abc'
    print(findAnagrams(s,p))

if __name__ == '__main__':
    main()
            