#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

res = requests.post('http://localhost:8090/studentAdd',
                    json={
                        "age": 19,
                        "email": "345@qq.com",
                        "id": 2020,
                        "name": "zhangsan",
                        "sex": "男"
                    })

print(res.json())
# print(res.status_code)
# print(res.content.decode('utf8'))
