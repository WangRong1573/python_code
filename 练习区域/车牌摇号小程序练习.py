#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 使用random
import random


# random.choice()  从'abcdefg...'参数中随机选择一个，参数也可以是一个列表，随机选择列表的一个值
# a = ['a','b','c','d','r','t','y']
# print(random.sample(a, 3)) 从元素中随机选择n个
# random.randint(1,100) 生成随机数[1,100)

# 需求：摇号小程序，实现摇号功能选择车牌
# 可选择三次
# 可选择的车牌个数为20个
# 车牌号为京A-Z，其他5位为随机数

def creat_no():
    print('可选的车牌号有：')
    for i in range(1, 21):
        num = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nums = 'abcdefghijklmnopqrstuvwxyz0123456789'
        city = '京'
        no = random.choice(num)
        no2 = ''.join(random.sample(nums, 5))
        carNo = city + no + '.' + no2
        if i == 11:
            print()
        print(carNo, end='\t')
    print()


def chose():
    count = 1
    while count <= 3:
        creat_no()
        choice = input('是否有您心仪的车牌？')
        if choice == 'y':
            print('恭喜你')
            break
        else:
            count += 1
            print('请继续选择：')
            if count == 4:
                print('对不起您的次数已用完')
                break
            print(f'温馨提示：您还有{3 - count}次选择机会')
            continue

chose()