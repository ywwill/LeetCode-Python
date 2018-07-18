# !usr/bin/python
# -*- coding:utf-8 -*-

def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    sum = 0
    for i in digits:
        sum = sum * 10 + i
    return [int(x) for x in str(sum+1)] 


def main():
   digits = [1,2,3,4,5,6]
   print(plusOne(digits))

if __name__ == '__main__':
    main()