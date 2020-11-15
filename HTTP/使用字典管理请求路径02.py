#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
from wsgiref import simple_server
from wsgiref.simple_server import make_server


def load_file(file_name, **kwargs):
    try:
        with open('../pages/' + file_name, 'r', encoding='utf8') as file:
            content = file.read()
            if kwargs:
                content = content.format(**kwargs)
            return content
    except FileNotFoundError:
        print('文件未找到')


def my_page():
    return '欢迎来到首页'


def test():
    return json.dumps({'name': 'jack', 'age': 18})

def login():
    return load_file('login2.txt')


def demo():
    return load_file('hello.html').format(name='tom', gender='男', age=19)


url = {'/': my_page, '/test': test, '/login': login, '/demo': demo}


def demo_app(environ, start_response):
    path = environ['PATH_INFO']
    status_code = '200 OK'

    method = url.get(path)
    if method:
        response = method()
    # if path == '/':
    #     response = my_page()
    # elif path == '/test':
    #     response = test()
    # elif path == '/login':
    #     response = login()
    # elif path == '/demo':
    #     response = demo()
    else:
        status_code = '404 Page Not Found'
        response = '页面走丢了'

    start_response(status_code, [('Content-Type', 'text/html;charset=utf8')])
    return [response.encode('utf8')]


if __name__ == '__main__':
    httpd_server = make_server('', 8000, demo_app)
    sa = httpd_server.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    httpd_server.serve_forever()
