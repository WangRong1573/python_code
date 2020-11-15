#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 外层循环控制行数
# 内层循环小于外层循环

for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{i} * {j} = {i * j}',end='\t')
    print()
