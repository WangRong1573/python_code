#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pprint import pprint

import requests

res = requests.get('http://localhost:8090/students')
print(res.status_code)

pprint(res.json(),width=30)