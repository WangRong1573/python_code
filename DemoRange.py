# range函数
'''第一种方式：只给一个参数'''
r = range(10)
print(list(r))

'''两个参数range(start,end),相差都是1'''
l = range(1, 10)
print(list(l))

'''三个参数range(start,end,step) step代表步长，即相差值'''
s = range(1, 10, 2)
print(list(s))

'''判断指定的数 是否在 in ， not in'''
print(10 in s)

print(10 not in s)


