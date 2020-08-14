#   字符串和编码


#   字符串是以Unicode编码

#   ord()函数获取字符的整数表示
print(ord('A'))
print(ord('中'))

#   chr()函数把编码转换为对应的字符
print(chr(65))
print(chr(20013))

# Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
#
# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
#
# x = b'ABC'
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
#
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes

# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
#
# 在bytes中，无法显示为ASCII字符的字节，用\x##显示。
#
# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
#
# >>> b'ABC'.decode('ascii')
# 'ABC'
# >>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
# '中文'

#   计算str包含多少个字符，可以用len()函数
print(len('中国人'))
print(len('abcd'))


#   格式化
# >>> 'Hello, %s' % 'world'
# 'Hello, world'
# >>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
# 'Hi, Michael, you have $1000000.'

# 占位符	替换内容
# %d	整数
# %f	浮点数  %.2f  可以设置保留几位小数
# %s	字符串
# %x	十六进制整数

print('hello,%s,you have %d$' % ('jack', 8888))
print('Growth Rate: %.2f%%' % 7.2)
