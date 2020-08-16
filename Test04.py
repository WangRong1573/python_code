# list是一种有序的集合，可以随时添加和删除其中的元素
classmates = ['Michael', 'Bob', 'Tracy']

# 用len()函数可以获得list元素的个数
len(classmates)

#   访问list中的元素采用下标方式，第一个是0，还可以访问最后一个元素 -1，倒数第二个-2
#   当索引超出了范围时，Python会报一个IndexError错误

#   向指定索引添加元素
classmates.insert(1, 'Tom')

print(classmates)

#   向末尾添加元素 append
classmates.append('John')

#   删除list末尾的元素
classmates.pop()

#   删除指定位置的元素
classmates.pop(1)

#   list里面的元素的数据类型也可以不同

# list元素也可以是另一个list，比如：
#
# >>> s = ['python', 'java', ['asp', 'php'], 'scheme']


#   tuple  tuple一旦初始化就不能修改
classmates1 = ('Michael', 'Bob', 'Tracy')

# >>> t = ('a', 'b', ['A', 'B'])
# >>> t[2][0] = 'X'
# >>> t[2][1] = 'Y'
# >>> t
# ('a', 'b', ['X', 'Y'])
# 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，
# 所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！


