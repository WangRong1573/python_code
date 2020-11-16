#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pprint import pprint

import requests

res = requests.get('http://localhost:8090/students')
print('-----------------------post前----------------------------------')
res_before = res.json()
pprint(res_before, width=30)
list_before = res_before['data']

resp = requests.post('http://localhost:8090/studentAdd',
                     json={
                         "age": 99,
                         "email": "8@qq.com",
                         "name": "tom",
                         "sex": "nv"
                     })
resp.json()

print('-----------------------post后----------------------------------')
res_after = res.json()
pprint(res_after, width=30)
list_after = res_after['data']

# 取出多出来的人
new_people = None

for p in list_after:
    if p not in list_before:
        new_people = p
        break

# 检查是否是添加的人
assert new_people is not None
assert new_people['age'] == 99
assert new_people['email'] == '8@qq.com'
assert new_people['name'] == 'tom'
assert new_people['sex'] == 'nv'

print('============ test pass ================')
