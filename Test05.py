#   条件判断

age = 3
if age > 18:
    print('成年人')
else:
    print('未成年人')


#   if...elif...else
num = 10
if num > 5:
    print('这个数大于5')
elif num > 10:
    print('这个数大于10')
else:
    print('这个数很小')


#    input     返回的数据类型是str
s = input('birth: ')
birth = int(s)
if birth > 2000:
    print('00后')
else:
    print('00前')



