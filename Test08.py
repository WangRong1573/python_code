#   字符串
str1 = 'i love you'
print(str1[1:5])

#   将字符串的第一个元素变成大写
print(str1.capitalize())

#   将字符串所有字符变成小写
print(str1.casefold())

#   字符串居中，center(width) 使用空格填充至长度width的新字符串
print(str1.center(40))

#   返回sub在字符串里出现的次数，count(sub, [start, end]) start和end参数表示范围，可选参数
print(str1.count('o', 1, 6))
print(str1.count('m'))  # 0

#   判断字符串是否以某某结尾
print(str1.endswith('u'))

#   find(sub,[start,end]) 检测sub是否包含在字符串中，有返回索引值；没有返回-1，start和end参数表示范围，可选参数
print(str1.find('o'))

#   index(sub,[start,end])

#   去掉字符串左边的空格
str2 = '    i love you  1 1 '
print(str2.lstrip())

#   去掉字符串左右空格
print(str2.strip())
