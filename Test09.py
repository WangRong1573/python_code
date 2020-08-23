"""lambda表达式"""

"""普通方法定义"""


def test(x):
    return x * 2


test(5)

#   lambda表达式写法

g = lambda x: x * 2
g(5)

"""filter()"""
#   filter(None,[1,0,False,True]) 可根据筛选条件过滤内容，None可传入的筛选条件，第二个参数为需要过滤的对象
l = filter(None, [1, 0, False, True])
print(list(l))
#   过滤20以内的奇数
f = lambda y: y % 2
temp = range(1, 20)
print(list(filter(f, temp)))

print(list(map(lambda x: x * 2, range(20))))
