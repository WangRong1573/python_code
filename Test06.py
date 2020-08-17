#   数组
mebers = ['tom', 'john', 'jack', 'luk', 'jo', 'a']

mix = [1, 3.14, [1, 2, 3], "aaa"]

#   数组长度
print(len(mebers))

#   添加元素 append() 只有一个参数
mebers.append('葫芦娃')

#   添加元素 原理：使用一个数组来拓展另外一个数组
mebers.extend(['b', 'D'])
print(mebers)

#   插入元素
mebers.insert(0, '钢铁侠')
print(mebers)

#   删除元素
mebers.remove('a')
print(mebers)

#   删除不存在元素时会报异常

#   删除元素2
del mebers[0]

#   删除元素3  pop()删除最后一个元素并返回
mebers.pop()
#   删除指定索引元素
mebers.pop(1)

#   分片
num = [1, 6, 3, 8, 7, 9, 54, 654, 5, 45, 4, 54]
#   从索引1开始截取 [1,3)但是不包括索引3
print(num[1:3])
#   从0开始可以省略0
print(num[:3])
#   全部拷贝可以省略
print(num[:])
#   拷贝最后一个元素
print(num[-1:])
print(num[-2:])

print('葫芦娃' not in num)
#   数组排序
num.sort()
print(num)
#   返回元素所在索引
num.index(6)

#   数组倒序排列
num.reverse()

# 数组拷贝要使用分片 num[:]

#   数组拼接不要使用"+"号，要使用append()方法
