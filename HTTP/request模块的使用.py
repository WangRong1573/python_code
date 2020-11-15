#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

response = requests.get('http://localhost:8000/test')
# get的结果是一个response对象
# print(response)

# content指的是返回的结果，是一个二进制，可以用来传递图片
print(response.content.decode('utf8'))

# text 也是返回结果，直接是文本内容
print(response.text)
print(type(response.text))

# 状态码
print(response.status_code)

# 如果返回结果是一个json字符串，可以解析json字符串
# 把json字符串解析成为Python里对应的数据类型：字典、列表等
print(response.json(),type(response.json()))