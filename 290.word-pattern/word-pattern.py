# !usr/bin/python
# -*- coding:utf-8 -*-

def wordPattern(pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    # 类似于205题
    '''
    .pattern和str的length
    .zip连接pattern和str按空格分割后的值
    .比较三者的length
    '''

    return len(pattern) == len(str.split(' ')) and len(set(zip(pattern, str.split(' '))))  == len(set(pattern)) == len(set(str.split(' '))) 

def testFunc(pattern, str):
    result = str + ' --> ' + pattern + ' --> '
    print(result, wordPattern(pattern, str))

def main():
    testFunc('abba', 'dog cat cat dog')
    testFunc('abba', 'dog cat cat fish')
    testFunc('aaaa', 'dog dog dog dog')
    testFunc('abba', 'dog dog dog dog')

if __name__ == '__main__':
    main()