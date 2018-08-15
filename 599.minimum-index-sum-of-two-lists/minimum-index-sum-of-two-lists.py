# !usr/bin/python
# -*- coding:utf-8 -*-

'''
题意：两个列表找出相同的字符串，
若只有一个，就输出这一个。
若有多组，则选择下标和最小的一组
'''

def findRestaurant(list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    dic1 = {v:i for i, v in enumerate(list1)}
    best, ans = 1e9, [] #best初始化为一个很大的数值

    for i,v in enumerate(list2):
        if v in dic1:
            if i + dic1[v] < best:
                best = i + dic1[v]
                ans = [v]
            elif i + dic1[v] == best: #存在多个选项
                ans.append(v)
    return best, ans

def main():
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]

    list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

    list3 = ["Shogun", "KFC", "Burger King", "Tapioca Express"]

    list4 = ["KFC", "Shogun", "Burger King"]

    print(findRestaurant(list1, list2))

    print(findRestaurant(list3, list4))


if __name__ == '__main__':
    main()   
            
            