# !usr/bin/python
# -*- coding:utf-8 -*-

'''
因为是平均分配,所以姐姐获得的不同糖果的个数最多为n／2,如果种类超过n/2,那么姐姐可以获得n/2种，否则可以获得的是种类的最大值
'''

def distributeCandies1(candies):
    """
    :type candies: List[int]
    :rtype: int
    """
    return len(set(candies)) if len(set(candies)) < len(candies) / 2 else len(candies) / 2

def distributeCandies2(candies):
    """
    :type candies: List[int]
    :rtype: int
    """
    return min(len(candies) / 2, len(set(candies)))

def main():
    candies1 = [1,1,2,2,3,3]
    candies2 = [1,1,2,3]

    print(distributeCandies1(candies1))
    print(distributeCandies1(candies2))

    print(distributeCandies2(candies1))
    print(distributeCandies2(candies2))

if __name__ == '__main__':
    main()