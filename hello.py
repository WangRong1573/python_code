import random

# Python使用缩进来组织代码块，请务必遵守约定俗成的习惯，坚持使用4个空格的缩进。

# 在文本编辑器中，需要设置把Tab自动转换为4个空格，确保不混用Tab和空格。
sec = random.randint(1, 10)
print('---一起来玩猜数字游戏吧----')
temp = input('请输入你猜的数字')
guess = int(temp)
while guess != sec:
    print('猜错了哦，请继续输入吧：')
    temp = input()
    guess = int(temp)
    if guess == sec:
        print('恭喜你猜对了哦')
    elif guess > sec:
        print('大了，小一点试试')
    else:
        print('猜小了，大一点试试')
print('游戏结束，欢迎下次来玩')
