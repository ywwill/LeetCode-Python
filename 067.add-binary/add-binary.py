# !usr/bin/python
# -*- coding:utf-8 -*-

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    if a == '':
        return b
    if b == '':
        return a
    if a[-1] == '1' and b[-1] == '1':
        return addBinary(addBinary(a[:-1], b[:-1]), '1') + '0'
    elif a[-1] == '0' and b[-1] == '0':
        return addBinary(a[:-1], b[:-1]) + '0'
    else:
        return addBinary(a[:-1], b[:-1]) + '1'


def main():
    a = "1010"
    b = "1011"
    print(addBinary(a,b))

if __name__ == '__main__':
    main()
            